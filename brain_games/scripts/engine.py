#!/usr/bin/env python
import prompt


def main(q_and_a):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, { name }!")
    main_question = q_and_a["main question"]
    print(f"{ main_question }")
    count = 0
    questions = q_and_a["questions"]
    answers = q_and_a["answers"]
    for i in range(0, 3):
        answer_from_user = prompt.string(questions[i])
        print(f"Your answer: { answer_from_user }")
        right_answer = answers[i]
        if answer_from_user == right_answer:
            print("Correct!")
            count += 1
        else:
            string_to_ans1 = f"'{ answer_from_user }' is wrong answer ;(. "
            string_to_ans2 = f"Correct answer was '{ right_answer }'."
            print(string_to_ans1 + string_to_ans2)
            break
    if count == 3:
        print(f"Congratulations, { name }!")
    else:
        print(f"Let's try again, { name }!")


if __name__ == '__main__':
    main()
