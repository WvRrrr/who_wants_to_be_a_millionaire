import json
import random


# adds a loading questions from a provided json file
def load_questions(file_path):
    with open(file_path, 'r') as file:
        questions_data = json.load(file)
    return questions_data

