# This project will calculate and display travel expenses
# 26 September 2022
# CTI-110 P1HW2 - Travel Expenses
# Laken Sanders

print('This program calculates and displays travel expenses')
print()

print('Enter Budget:', end=' ')
budget = float(input())
print()

print('Enter your travel destination:', end=' ')
travelDest = input()
print()

print('How much do you think you will spend on gas?', end=' ')
gasCost = float(input())
print()

print('Approximately, how much will you need for accomodation/hotel?', end=' ')
hotelCost = float(input())
print()

print('Last, how much do you need for food?', end=' ')
foodCost = float(input())
print()

remain_balance = (budget-(gasCost + hotelCost + foodCost))

print('------------Travel Expenses------------')
print('Location:', travelDest)
print('Initial Budget:', budget)
print()
print('Fuel:', gasCost)
print('Accomodation:', hotelCost)
print('Food:', foodCost)
print()
print('Remaining Balance:', remain_balance)

# Ask user to input buget
# Input budget as float
# Ask user to input travel destination
# Input travelDest
# Ask user to input amount they will spend on gas
# Input gasCosts as float
# Ask user to input amount they will spend on accomodation
# Input hotelCosts as float
# Ask user to input amount they will spend on food
# Input foodCosts as float
# Add all expenses and subtract from budget to get new variable, remain_Balance
# Display Travel Expenses such as:
# Location:
# Initial Budget:
#
# Fuel:
# Accommodation:
# Food:
#
# Remaining Balance:
    
