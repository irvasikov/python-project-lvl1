#!/usr/bin/env python
from random import randint
from brain_games.scripts import engine


def even_number_or_not(number: int) -> str:
    """Define even number or not and return str yes or not"""
    answer = "yes" if int(number) % 2 == 0 else "no"
    return answer


def get_random_number() -> int:
    """Get random number with use module random"""
    num = randint(1, 101)
    return num


def main():
    """Main function in this module"""
    main_question = 'Answer "yes" if the number is even, otherwise answer "no".'
    q_and_a = {
        "main question": main_question,
        "answers": [],
        "questions": [],
    }
    for i in range(0, 3):
        number = get_random_number()
        question = f"Question: { number }"
        right_answer = even_number_or_not(number)
        q_and_a["questions"].append(question)
        q_and_a["answers"].append(right_answer)
    engine.main(q_and_a)


if __name__ == "__main__":
    main()
