#!/usr/bin/env python
# coding: utf-8

import random
from IPython.display import clear_output

while True:
    
    while True:
        digits = input("How many digits would you like to play? (3 or 4): ")
        #print(digits, type(digits))
        if digits in ["3", "4"]:
            break
        else:
            print("Wrong input! Try again.")
    digits = int(digits)

    question = ""
    while len(question) != digits:
        temp_num = random.randrange(10)
        temp_num = str(temp_num)
        #print(temp_num)
        if temp_num not in question:
            question += temp_num
    print(question)

    while True:
        while True:
            answer = input("Guess the number (%s digits): " % digits)
            if len(answer) == digits and answer.isdigit():
                break
            else:
                print("Wrong input! Try again.")
        answer = str(answer)

        if answer == question:
            print("Congratulation! You win the game!")
            break

        solution = {"S":0, "B":0}
        for x in range(digits):
            temp_num_position = question.find(answer[x])
            if temp_num_position == -1:
                continue
            if temp_num_position == x:
                solution["S"] += 1
            else:
                solution["B"] += 1
        #print(solution)

        temp_answer = "%sS%sB" % (solution["S"], solution["B"])
        if temp_answer == "0S0B":
            temp_answer = "OUT"
        print(temp_answer)
    
    while True:
        play_again = input("Do you want to play one more game? (Y/N): ")
        play_again = play_again.upper()
        if play_again in ["YES", "Y", "NO", "N"]:
            clear_output()
            break
        else:
            print("Wrong input! Try again.")

    if play_again in ["NO", "N"]:
        break

print("Thank you for playing.")
