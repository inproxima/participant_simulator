# IMPORTS ######################################################################
import json
import os
import openai
from time import time,sleep
import textwrap
import re
from flask import Flask, redirect, render_template, request, url_for


def save_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as outfile:
        outfile.write(content)

def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()

# GLOBAL VARIABLES 
app = Flask(__name__)  

persona = ""  # Chatbot personality trait(s)
key = ""
model = ""  # Fine-tuned GPT-3 model to allow to use to choose model for later version of the program .
temperature = None  # GPT-3 parameter to allow to use to choose model for later version of the program.
prev_human = "Hello."  # Previous human message, starting with Hello. Could also be empty. 
prev_bot = "Hi."  # Previous AI message, starting with Hi. Could also be empty. 

# Prompt

def generate_prompt(human_input):
    """Generates the prompt for the GPT-3 generation.

    Args:
        human_input: the current utterance string from the user.

    Returns:
        GPT-3 prompt with the AI persona and past three turns.
    """
    global persona
    global prev_human
    global prev_bot

    prompt = """The following is a research interview between a researcher and a participant. The participant has the following persona: {persona}.
    
    Human: {prev_human}
    {persona}: {prev_bot}
    Human: {human_input}
    {persona}:""".format(persona=persona, prev_human=prev_human, prev_bot=prev_bot, human_input=human_input)

    return prompt


# CHATBOT API 


@app.route("/", methods=["GET", "POST"])
def index():
    """GETs and POSTs information for the home page.

    Returns:
        Rendered template for the home page (index.html).
    """
    # If the user is POSTing information to the server, update global variables.
    if request.method == "POST":
        global key
        key = request.form["key"]
        
        global persona
        persona = request.form["persona"]

        global model
        model = "text-davinci-003"

        global temperature
        temperature = "0.7"

        openai.api_key = key

        # Redirect the web page to the chatbot interface.
        # The persona_description will appear at the top of the web page with
        # the user's input filled in. Notice that the chat() API function will
        # use persona_description when the user makes a GET request, so we have
        # to provide the information here.
        return redirect(url_for(
            "chat",
            persona_description="AI Generated Persona: {}".format(persona)))
            

    # If the user is GETting the home page, render and return it.
    return render_template("index.html")



@app.route("/chat", methods=["GET"])
def chat():
    """GETs information for the chatbot interface page.

    This function handles actions related to the chatbot interface page. Notice
    that we do not need a method for POST because the user does not submit new
    data to the server. All of the chat bubbles are added dynamically through
    JavaScript onto a static page.

    Returns:
        Rendered template for chatbot interface page (chatbot.html).
    """
    # Remember: the persona_description is populated by the index() API method.
    persona_description = request.args.get("persona_description")
    return render_template("chatbot.html",
                           persona_description=persona_description)


@app.route("/gpt3", methods=["GET"])
def get_bot_reply():
    # Retrieve human_input populated by getResponse script in chatbot.html.
    human_input = request.args.get("human_input")
    prompt = generate_prompt(human_input)

    # Query OpenAI API for GPT-3 generation.
    global model
    global temperature
    global persona
    
    try:
        response = openai.Completion.create(
            engine=model,
            prompt=prompt,
            temperature=0.7,
            max_tokens=250,
            stop=[f"{persona}:", "Human:", "\n"],
        ).choices[0].text
        is_successful = True
    except Exception as e:
        response = f"ERROR: {e}"
        is_successful = False

    # Update global variables
    global prev_human
    prev_human = human_input
    global prev_bot
    prev_bot = response

    output = {
        "response": response,
        "success": is_successful,
    }

    return json.dumps(output)


