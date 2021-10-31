# Calculating Grades (ok, let me think about this one)


# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average  Grade
# 90+  A
# 80-89    B
# 70-79    C
# 60-69    D
# 0-59 F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student is failing.

exam_one = int(input("Input exam grade one: "))

#exam_two = int(input("Input exam grade two: ")
exam_two = input("Input exam grade two: ") 

#exam_three = int(input("Input exam grade three: ")
exam_three = str(input("Input exam grade three: "))

grades = [exam_one,exam_two,exam_three]
sum = 0
'''
grade : loop variable, grades: list

for grade in grades:
    sum = sum + grade
'''

for grades in grades:
  sum = str(input(sum + grades))

avg = sum / len(grades)

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 89:
    letter_grade = "B"
''' 
C : 70-79, D: 60-69, F: 0-59

elif avg >= 70 and avg < 79:
    letter_grade = "C"
elif avg >= 60 and avg < 69:
    letter_grade = "D"
elif avg >= 0 and avg < 59:
    letter_grade = "F"

'''
    
elif avg > 70 and avg < 79:
    letter_grade = "C"
elif avg <= 60 and avg >= 69:
    letter_grade = "D"
elif avg <= 0 and avg >=59:
    letter_grade = "F"

for grade in grades:
    print("Exam: " + str(grade))

'''
Average and Grade should be printed once.
No indentation for those printe statements

print("Average: " + str(avg))
print("Grade: " + letter_grade)
'''
    
    print("Average: " + str(avg))

    print("Grade: " + letter_grade)

if letter_grade == "F":
    print("Student is failing.")
else:
    print("Student is passing.")
#I added a colon in line 37. I removed the extra parenthesis. I added a double quote. I added an extra line for grade F and added parenthesis
#for line 56.I changed line 53 to include double equal marks.
