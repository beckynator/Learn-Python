import random

# Create a list of questions and answers.
questions = [
    ("What is the capital of France?", "Paris"),
    ("What is the largest ocean in the world?", "Pacific Ocean"),
    ("Who is the president of the United States?", "Joe Biden"),
]

# Create a function to generate a random question from the list.
def get_random_question():
    return random.choice(questions)

# Create a function to check a user's answer.
def check_answer(question, answer):
    if answer == questions[question][1]:
        return True
    return False
# Create a function to play the quiz game.
def play_quiz():
    score = 0
    for question in questions:
        answer = input("What is the answer to " + question[0] + "? ")
        if check_answer(question, answer):
            score += 1
    print("You scored " + str(score) + " out of " + str(len(questions)) + ".")

# Start the quiz game.
play_quiz()
