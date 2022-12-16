# Participant Simulator
Welcome to the GPT-3 Participant Simulator! This is a small web app that queries the OpenAI
API to make a chatbot powered by GPT-3. The chatbot also takes a personal, which and you can interview it for research purposes. 

A lot of this code (and basically all of the README!) was adapted from the
OpenAI [Quickstart Tutorial](https://github.com/openai/openai-quickstart-python)
for Python.

## Setup
1. If you don’t have Python installed, install it from here

2. Clone this repository

3. Navigate into the project directory

```
$ cd gpt3-chatbot
```

4. Create a new virtual environment

```
$ python -m venv venv
$ . venv/bin/activate
```

5. Install the requirements

```
$ pip install -r requirements.txt
```

6. Make a copy of the example environment variables file

```
$ cp .env.example .env
```

7. Add your [API key](https://beta.openai.com/account/api-keys) to the newly
created .env file

8. Run the app

```
$ flask run
```

You should now be able to access the app at http://localhost:5000!
