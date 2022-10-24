# CTI-110
# P2HW2 - List
# Laken Sanders
# 17 October 2022

module_1 = float(input('Enter grade for Module 1:'))
module_2 = float(input('Enter grade for Module 2:'))
module_3 = float(input('Enter grade for Module 3:'))
module_4 = float(input('Enter grade for Module 4:'))
module_5 = float(input('Enter grade for Module 5:'))
module_6 = float(input('Enter grade for Module 6:'))
print()

allModuleGrades = [module_1, module_2, module_3, module_4, module_5, module_6]

average = (sum(allModuleGrades)) / len(allModuleGrades)


print('------------Results------------')
print('Lowest Grade:      ', min(allModuleGrades))
print('Highest Grade:     ', max(allModuleGrades))
print('Sum of Grades:     ', sum(allModuleGrades))
print('Average:           ', (f'{average:.2f}'))
print('----------------------------------------')

# Get 6 grade inputs from user, assigning each a variable.
# Create a list that includes all grades.
# Output min and max of grades as lowest and highest grade
# Output sum and average of grades
