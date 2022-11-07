# CTI-110
# P3HW1-Debugging
# Laken Sanders
# 26 October 2022

#This program takes a number grade from each module, determines lowest grade, highest grade, sum of grades, and average and displays letter grade for average.

#Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

#Add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

#Determine lowest, highest, sum, and average for grades

low = min(grades)
high = max(grades)
gradesSum = sum(grades)
avg = gradesSum / len(grades)

#Output results of lowest, highest, sum, and average

print()
print('------------Results------------')
print('Lowest Grade:       ', low)
print('Highest Grade:      ', high)
print('Sum of Grades:      ', gradesSum)
print('Average:            ', (f'{avg:.2f}'))
print('----------------------------------------')

#Determine letter grade for average and output results

if avg >= 90:
    print('Your grade is: A')
elif avg >= 80:
    print('Your grade is: B')
elif avg >= 70:
    print('Your grade is: C')
elif avg >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F')
