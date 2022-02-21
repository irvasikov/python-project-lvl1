#!/usr/bin/env python
import random
from brain_games.scripts import engine


def progression():
    step = random.randint(0, 6)
    start_num = random.randint(0, 21)
    numbers = []
    for i in range(0, 10):
        y = start_num + i * step
        numbers.append(y)
    rand = random.randint(1, 9)
    right_answer = numbers[rand]
    numbers[rand] = ".."
    return (numbers, str(right_answer))


def main():
    """Main function in this module"""
    main_question = "What number is missing in the progression?"
    q_and_a = {
        "main question": main_question,
        "answers": [],
        "questions": [],
    }
    for i in range(0, 3):
        numbers, right_answer = progression()
        str_numbers = " ".join(list(map(str, numbers)))
        question = f"Question: { str_numbers }"
        q_and_a["questions"].append(question)
        q_and_a["answers"].append(right_answer)
    engine.main(q_and_a)


if __name__ == "__main__":
    main()
