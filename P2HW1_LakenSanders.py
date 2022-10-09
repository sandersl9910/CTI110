# This project will calculate and display travel expenses
# 9 October 2022
# CTI-110 P2HW1 - Travel
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

dollarSign = '$'
dollarBudget = dollarSign + str(budget)
dollarGas = dollarSign + str(gasCost)
dollarHotel = dollarSign + str(hotelCost)
dollarFood = dollarSign + str(foodCost)
dollarRemaining = dollarSign + str(remain_balance)

print('------------Travel Expenses------------')
print('Location:            ', travelDest)
print('Initial Budget:      ', dollarBudget)
print('Fuel:                ', dollarGas)
print('Accomodation:        ', dollarHotel)
print('Food:                ', dollarFood)
print('----------------------------------------')
print()
print('Remaining Balance:   ', dollarRemaining)

# Ask user to input buget.
# Input budget as float.
# Ask user to input travel destination.
# Input travelDest.
# Ask user to input amount they will spend on gas.
# Input gasCosts as float.
# Ask user to input amount they will spend on accomodation.
# Input hotelCosts as float.
# Ask user to input amount they will spend on food.
# Input foodCosts as float.
# Add all expenses and subtract from budget to get new variable, remain_Balance.
# Create new string, dollarSign, that holds '$'.
# Create a new variable for each expense that concatenates dollarSign and the
# string literal of original expense variables such as budget, gasCost, etc.
#
# Display Travel Expenses such as:
#
# ------------Travel Expenses------------
# Location:
# Initial Budget:
# Fuel:
# Accommodation:
# Food:
# ----------------------------------------
#
# Remaining Balance:
