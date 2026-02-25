# --- Login system ---
admin_username = "admin"
admin_password = "pass"

username = input("Enter your username: ")
password = input("Enter your password: ")

# and: &&: all have to be true
# or: ||: only one needs to be true
is_logged_in = username == admin_username and password == admin_password
if is_logged_in:
    print("Step 1: username was correct.")
    print("Step 2: password was correct.")
else:
    print("Invalid credentials")

# !: or example
# age = 15
# exam_score = 50
# are_your_cool = age >= 18 or exam_score >= 60
# print(are_your_cool) 