is_running = True
while is_running:
    # Print a Menu of options that the user can choose
    print("--- Menu ---")
    print("1. Print fruits in your home")
    print("2. Surprise me")
    print("0. Exit")
    print("------------\n")

    # Get user input
    menu_choice = input("Enter your choice: ")

    # Based on that input do different things
    if menu_choice == "1":
        for fruit in ["Apples", "Bananas", "Fruits"]:
            print(f"- {fruit}")
    elif menu_choice == "2":
        print("- Surprise!")
    elif menu_choice == "0":
        is_running = False
        print("Terminating program...")
    else:
        print("- Invalid choice, try again.")
