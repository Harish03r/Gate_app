import random
import json
import time

# Load syllabus-based questions (backup to AI generation)
with open("dataset.jsonl", "r") as f:
    QUESTIONS = json.load(f)

def generate_test(num_questions=65):
    return random.sample(QUESTIONS, num_questions)

def evaluate_test(responses):
    score = 0
    details = []
    for q in responses:
        if q["type"] == "MCQ":
            if q["user_answer"] == q["correct"]:
                score += q["marks"]
            else:
                score -= 0.33 if q["marks"] == 1 else 0.66
        elif q["type"] in ["MSQ", "NAT"]:
            if q["user_answer"] == q["correct"]:
                score += q["marks"]

        details.append({"q": q["question"], "your_ans": q["user_answer"], "correct": q["correct"]})
    return score, details
