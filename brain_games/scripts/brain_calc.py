#!/usr/bin/env python
import random
import engine


def calc():
    sings = ("+", "-", "*")
    sing = random.randint(0, 2)
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    znak = sings[sing]
    stroka = f"{ num1 } {znak} { num2 }"
    if sings[sing] == "+":
        right_answer = num1 + num2
    elif sings[sing] == "-":
        right_answer = num1 - num2
    else:
        right_answer = num1 * num2
    return (stroka, str(right_answer))


def main():
    main_question = "What is the result of the expression?"
    q_and_a = {
        "main question": main_question,
        "questions": [],
        "answers": [],
    }
    for i in range(0, 3):
        q, a = calc()
        q_and_a["questions"].append(q)
        q_and_a["answers"].append(a)
    engine.main(q_and_a)


if __name__ == '__main__':
    main()
