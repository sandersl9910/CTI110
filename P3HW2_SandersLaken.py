# CTI-110-0001
# P3HW2-Salary
# Laken Sanders
# 31 October 2022

# This program takes user's name, number of hours worked this week, and pay rate and outputs a basic layout of
# a paystub including name, pay rate, number of hours worked, overtime hours, overtime pay, pay for regular hours,
# and gross pay


# Get user's name, hours worked, and pay rate

userName = input("Enter employee's name: ")
allHours = float(input('Enter number of hours worked: '))
payRate = float(input("Enter employee's pay rate: "))
print('-------------------------------------')

# Calculations

overTimeHours = 0.0
overTimePay = 0.0
regHours = 0.0
regHourPay = 0.0

if allHours > 40:
    overTimeHours = allHours - 40
    regHours = 40
else:
    regHours = allHours

regHourPay = regHours * payRate

if overTimeHours > 0:
    overTimePay = overTimeHours * (payRate * 1.5)


grossPay = regHourPay + overTimePay

# Output

print('Employee name:   ', userName)
print()
print('Hours Worked     Pay Rate     OverTime     OverTime Pay     RegHour Pay     Gross Pay')
print('----------------------------------------------------------------------------------------------')
print(f'{allHours:<17.1f}{payRate:<13.1f}{overTimeHours:<12.1f}','$' f'{overTimePay:<16.2f}' '$' f'{regHourPay:<15.2f}' '$' f'{grossPay:.2f}')


# Get employee name, number of hours worked this week, and pay rate from user
# Evalute if employee has worked overtime
# Calculate amount employee should be paid for regular hours worked
# Calculate amount employee should be paid for overtime if applicable
# Calculate gross pay using regular and overtime hours
# Display employee name, hours worked, pay rate, overtime, overtime pay, regular hour pay, and gross pay

