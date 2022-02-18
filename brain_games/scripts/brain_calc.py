#!/usr/bin/env python
import prompt
import random


def calc():
    sings = ("+", "-", "*")
    sing = random.randint(0, 3)
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    stroka = f"{ num1 } {sings[sing]} { num2 }"
    if sings[sing] == "+":
        right_answer = num1 + num2
    elif sings[sing] == "-":
        right_answer = num1 - num2
    else:
        right_answer = num1 * num2
    return (stroka, right_answer)


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, { name }!")
    print("What is the result of the expression?")
    count = 0
    for i in range(0, 3):
        q_and_a = calc()
        answer_from_user = prompt.string(q_and_a[0])
        print(f"Your answer: { answer_from_user }")
        if answer_from_user == q_and_a[1]:
            print("Correct!")
            count += 1
        else:
            break
    if count == 3:
        print(f"Congratulations, { name }!")


if __name__ == '__main__':
    main()
