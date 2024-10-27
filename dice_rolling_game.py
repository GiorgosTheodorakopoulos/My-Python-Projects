import random

roll_count = 0

while True:
    option = input("Roll the dice? (y/n): ")
    if option.capitalize() == "Y":
        try:
            num_dice = int(input("How many dices would you like to roll? "))
            if num_dice <= 0:
                print("Please enter a positive integer")
                continue
            dice_rolls = [random.randint(1, 6) for _ in range(num_dice)]
            print("Dice rolls:", tuple(dice_rolls))
            roll_count += 1

        except ValueError:
            print("Invalid input.Please enter a positive integer.")
    elif option.capitalize() == "N":
        print("Thank you for playing!")
        print(f"You have rolled the dice {roll_count} time(s) during this session")
        break
    else:
        print("Invalid choice!")