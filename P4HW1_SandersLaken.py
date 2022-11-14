# CTI-110
# P4HW1-Score List
# Laken Sanders
# 14 November 2022

allModuleGrades = []

userNum = int(input('How many scores do you want to enter?'))

index = 1
while index <= userNum:
    print('Enter score #{}:'.format(index), end=' ')
    grade = float(input())

    if (grade < 0) or (grade > 100):
        print()
        print('INVALID Score entered!!!!')
        print('Score should be between 0 and 100')
        
    else:
        allModuleGrades.append(grade)
        index += 1
        
        


lowestGrade = min(allModuleGrades)
allModuleGrades.remove(lowestGrade)
averageGrade = (sum(allModuleGrades)) / len(allModuleGrades)

if averageGrade >= 90:
    grade = 'A'
elif averageGrade >= 80:
    grade = 'B'
elif averageGrade >= 70:
    grade = 'C'
elif averageGrade >= 60:
    grade = 'D'
else:
    grade = 'F'

print()
print()


print('------------Results------------')
print('Lowest Grade  :', lowestGrade)
print('Modified List :', allModuleGrades)
print('Scores Average:', (f'{averageGrade:.2f}'))
print('Grade         :', grade)
print('----------------------------------------')

# Get number of grades from user.
# Get scores from user and determine if valid.
# Add scores to a list.
# Calculate lowest score.
# Drop lowest score.
# Calculate average of scores.
# Output Lowest Score, Modified List, Scores Average, and Grade.
