import json

FILEPATH = "questions.json"

with open(FILEPATH, "r") as file:
    content = file.read()

data = json.loads(content)
score = 0
for question in data:
    print(question["question"])
    for index, alternative in enumerate(question["alternatives"]):
        print(f"{index+1} - {alternative}")
    user_input = int(input("Enter your answer: "))
    question["user_choice"] = user_input

    if question["correct_answer"] == question["user_choice"]:
        score += 1



print(f"Your Score: {score} / {len(data)}")