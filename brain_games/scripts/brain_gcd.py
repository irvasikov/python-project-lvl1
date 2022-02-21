#!/usr/bin/env python
import random
from brain_games.scripts import engine


def gcd_rem_division(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 %= num2
        else:
            num2 %= num1
    return num1 or num2


def main():
    main_question = "Find the greatest common divisor of given numbers."
    q_and_a = {
        "main question": main_question,
        "answers": [],
        "questions": [],
    }
    for i in range(0, 3):
        number1 = random.randint(1, 100)
        number2 = random.randint(1, 100)
        question = f"Question: { number1 } {number2}"
        right_answer = str(gcd_rem_division(number1, number2))
        q_and_a["questions"].append(question)
        q_and_a["answers"].append(right_answer)
    engine.main(q_and_a)


if __name__ == '__main__':
    main()
