# GPT-3 Chatbot
Welcome to our chatbot, powered by the state-of-the-art OpenAI GPT-3.5-Turbo model! This chatbot is a unique tool that can become a persona given by you, allowing it to be interviewed by student-researchers for educational purposes.

With the power of advanced natural language processing, this chatbot can understand and respond to a wide range of questions and topics, providing informative and engaging answers that can help students learn and explore various subjects


# Recognition
This project is funded by the 2023 Werklund School (University of Calgary) Teaching and Learning Support Grant. 

This bot was build on top of a model developed the [Alyssa Hwang](https://alyssahwang.com) as part of her PhD candidacy exam
(WPE-II for fellow Penn CIS people).

# Setup

    If you don’t have Python installed, install it from here

    Clone this repository

    Navigate into the project directory

$ cd gpt3-chatbot

    Create a new virtual environment

$ python -m venv venv
$ . venv/bin/activate

    Install the requirements

$ pip install -r requirements.txt

    Make a copy of the example environment variables file

$ cp .env.example .env

    Add your API key to the newly created .env file

    Run the app

$ flask run

You should now be able to access the app at http://localhost:5000!

