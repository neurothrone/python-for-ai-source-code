# --- Conditionals ---

# !: Comparison operators
# - equal to: ==
# - not equal to: !=
# - greater than: >
# - less than: <
# - greater than or equal: >=
# - less than or equal: <=

# !: if statement
#age = 15
#is_adult = age >= 18

#if (is_adult):
#    print("You are an adult.")

# --- Simple Grading system: Pass, Fail ---
# Grading by Exam: you can score from 0 to 100
# To pass you need 60 or greater
pass_grade = 60
student_score = 55

# !: if-else statement
# if student_score >= pass_grade:
#     print("You passed")
# else:
#     print("You failed")


# --- Advanced Grading system: A, B, C, D, E, F ---
# !: if-elif-else statement
# if student_score >= 95:
#     print("You got the grade A")
# elif student_score >= 90:
#     print("You got the grade B")
# elif student_score >= 80:
#     print("You got the grade C")
# elif student_score >= 70:
#     print("You got the grade D")
# elif student_score >= pass_grade:
#     print("You passed, you got an E")
# else:
#     print("You failed")

# Notes:
# Comment highlighted lines with Ctrl + K, C
# Uncomment highlighted lines with Ctrl + K, U

# !: Truthy and falsy values
is_computer_on = 0
if is_computer_on:
    print("On")
else:
    print("Off")
