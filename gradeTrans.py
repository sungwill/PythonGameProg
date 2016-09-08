import sys

print("This is a converter that converts numerical grade into letter grade.")

grade = sys.argv[1]
grade = float(grade)

if (grade < 60):
    letter = "F"
elif (grade >= 60 and grade < 63):
    letter = "D-"
elif (grade >= 63 and grade < 68):
    letter = "D"
elif (grade >= 68 and grade <= 69):
    letter = "D+"
elif (grade >= 70 and grade < 73):
    letter = "C-"
elif (grade >= 73 and grade < 78):
    letter = "C"
elif (grade >= 78 and grade <= 79):
    letter = "C+"
elif (grade >= 80 and grade < 83):
    letter = "B-"
elif (grade >= 83 and grade < 88):
    letter = "B"
elif (grade >= 88 and grade <= 89):
    letter = "B+"
elif (grade >= 90 and grade < 93):
    letter = "A-"
elif (grade >= 93 and grade < 97):
    letter = "A"
elif (grade >= 97 and grade <= 100):
    letter = "A+"

print("Your grade is ", letter)