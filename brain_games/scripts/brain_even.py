#!/usr/bin/env python
import prompt
from random import randint


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, { name }!")
    return name


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
    name = welcome_user()
    print("""Answer "yes" if the number is even, otherwise answer "no".""")
    count = 0
    while count != 3:
        number = get_random_number()
        answer_from_user = prompt.string(f"Question: { number }")
        print(f"Your answer: { answer_from_user }")
        right_answer = even_number_or_not(number)
        if answer_from_user != right_answer:
            string_to_ans1 = f"'{ answer_from_user }' is wrong answer ;(. "
            string_to_ans2 = f"Correct answer was '{ right_answer }'."
            print(string_to_ans1 + string_to_ans2)
            print(f"Let's try again, { name }!")
            count = 0
        else:
            print("Correct!")
            count += 1
    print(f"Congratulations, { name }!")


if __name__ == "__main__":
    main()
