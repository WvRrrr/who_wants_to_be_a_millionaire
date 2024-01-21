import json
import random

# Adds a loading questions from a provided json file
def load_questions(file_path):
    with open(file_path, 'r') as file:
        questions_data = json.load(file)
    return questions_data

# Display an answer and wait for input
def ask_question(question_data):
    print("\n" + "-"*40)
    print("\nQuestion: " + question_data["question"])
    options = ["A", "B", "C", "D"]

    for option in options:
        print(f"{option}: {question_data[option]}")

    user_answer = input("\nYour answer (A/B/C/D): ").upper()

    if user_answer == question_data["answer"]:
        print("Correct!")
        return True
    else:
        print(f"Wrong answer! The correct answer was {question_data['answer']}.")
        return False

# The actual game 
def millionaire_game(questions):
    print("\n\n\nWelcome to Who Wants to Be a Millionaire!")
    print("You will be presented with 10 multiple-choice questions.")
    print("For a good start you receive $1000 from us. Any correct answer will double your account balance. Answer all the questions correctly to win!")


    total_prize = 1000
    for i, question in enumerate(questions):
        print(f"\n\n\nQuestion {i + 1}:")

        if ask_question(question):
            total_prize *= 2
            if total_prize >= 1000000:
                print("Congratulations! That was the last question. Impressive knowledge! You've won $1,000,000!")
                break
            else:
                print(f"Your total prize money so far: ${total_prize}")
        else:
            print("\nGame Over! You leave with $" + "{:,}\n\n\n".format(total_prize))
            break

if __name__ == "__main__":
    questions_file_path = "Resources/questions.json" 
    questions_data = load_questions(questions_file_path)

    if questions_data:
        random.shuffle(questions_data)
        selected_questions = questions_data[:10]  # Select 10 random questions for the game
        millionaire_game(selected_questions)
    else:
        print("Error loading questions. Please check your JSON file.")