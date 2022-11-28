# This program asks user in a menu if they want to add or subtract random numbers, or exit program. Program evaluates if answer is right
# or wrong giving more chances when wrong. When answered correctly, congrats is given and number of guesses is displayed. Program
# then goes back to main menu for selection.
# 28 November 2022
# CTI-110 P5HW2 - Math Quiz
# Laken Sanders

import random

def user_menu():
    i = True
    while i == True:
        print('MAIN MENU')
        print('-------------------')
        print('1. Adding Random Numbers')
        print('2. Subtracting Random Numbers')
        print('3. Exit')
        print()
        print('Please choose one of the menu options:')

        userNum = int(input())

        if userNum == 1:
            adding_numbers()
        if userNum == 2:
            subtract_numbers()
        if userNum == 3:
            print('Thank you for playing...')
            print('Bye!!')
            i = False
            exit()
        if userNum != 1 and userNum != 2 and userNum !=3:
            print('Please enter 1, 2, or 3.')
            continue
        
def adding_numbers():
    num1 = random.randint(1,500)
    num2 = random.randint(1,500)
    right = num1 + num2
    print('  ', num1)
    print('+ ', num2)
    print()
    answer = int(input('Enter answer:'))
    guess = 1
    check_answer(answer, right, guess)

def subtract_numbers():
    num1 = random.randint(1,500)
    num2 = random.randint(1,500)
    right = num1 - num2
    print('  ', num1)
    print('- ', num2)
    print()
    answer = int(input('Enter answer:'))
    guess = 1
    check_answer(answer, right, guess)

def check_answer(answer, right, guess):
    if answer == right:
        correct_answer(answer, right,guess)
    else:
        wrong_answer(answer, right, guess)

    
def correct_answer(answer, right, guess):
        print('Congratulations!!!! Your answer is correct...')
        print('Number of guesses:', guess)
        print()
        user_menu()

def wrong_answer(answer, right, guess):
    if answer < right:
        print('Sorry, guess is too low.')
        print()
        answer = int(input('try again:'))
        guess += 1
        check_answer(answer, right, guess)
    elif answer > right:
        print('Sorry, guess is too high.')
        print()
        answer = int(input('try again:'))
        guess += 1
        check_answer(answer, right, guess)

user_menu()


    
