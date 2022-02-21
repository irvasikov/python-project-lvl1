#!/usr/bin/env python
import random
from brain_games.scripts import engine


def is_prime(num):
    for n in range(2, int(num ** (1 / 2)) + 1):
        if num % n == 0:
            return "no"
    return "yes"


def main():
    q1 = 'Answer "yes" if given number is prime. '
    q2 = 'Otherwise answer "no".'
    main_question = q1 + q2
    q_and_a = {
        "main question": main_question,
        "answers": [],
        "questions": [],
    }
    for i in range(0, 3):
        number = random.randint(1, 100)
        question = f"Question: { number }"
        right_answer = is_prime(number)
        q_and_a["questions"].append(question)
        q_and_a["answers"].append(right_answer)
    engine.main(q_and_a)


if __name__ == '__main__':
    main()
