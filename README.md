
## Features
- Interactive chatbot.
- Uses AJAX for form submission and to update the chatbox without page refresh.
- Uses Flask, a lightweight Python web framework.
- Integrates OpenAI's GPT-4 model for generating property descriptions.

## Project Structure
The project has a simple structure:
- `app.py` is the main Python script that handles the web server and the chatbot logic.
- `index.html` is the main webpage. It includes a simple chatbox and a form for user input.
- `questions.py` contains a Python dictionary with the chatbot states and questions.

## Installation

### Requirements
- Python 3.6 or above
- Flask web framework
- OpenAI Python client
- `fuzzywuzzy` for fuzzy string matching


To install the required packages, run:
```bash
pip install -r requirements.txt
