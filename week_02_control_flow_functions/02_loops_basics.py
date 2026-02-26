# --- Loops ---

# !: For loops

# name = "Captain"
# for character in name:
#     print("Step 1: Start")
#     print(f"Step 2: character: '{character}'")
#     print("Step 3: End")

# fruits = ["Apple", "Banana", "Pear"]
# for fruit in fruits:
#     print(fruit)

# numbers = [1, 2, 3, 4, 5]
# for num in numbers:
#     print(num)

for num in [1, 2, 3, 4, 5]:
    is_number_even = num % 2 == 0
    if is_number_even:
        continue

    print(num)

# for num in range(1, 6): # 1, 2, 3, 4, 5
#     print(num)

# !: While loops
# for item in items
# while condition

# number = 0
# while True:
#     # Identical
#     #number = number + 1
#     number += 1

#     if number > 5:
#         break

#     # I don't want to print even numbers
#     is_number_even = number % 2 == 0
#     if is_number_even:
#         continue
    
#     print(f"Number: {number}")
    
