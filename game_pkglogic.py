import random

def play_round():
    """Main logic for a single round of Stone Paper Scissors."""
    options = ["Stone", "Paper", "Scissors"]
    
    print("\n Match Started ")
    print("1. Stone")
    print("2. Paper")
    print("3. Scissors")
    
    user_input = input("Choose your weapon 1 to 3: ")
    
    if user_input not in ['1', '2', '3']:
        print("Invalid choice. Please pick 1 2 or 3.")
        return
        
    user_choice = options[int(user_input) - 1]
    comp_choice = random.choice(options)
    
    print("\nYour choice:", user_choice)
    print("Computer choice:", comp_choice)
    
    # Game rules
    if user_choice == comp_choice:
        print("Result: It is a Tie")
    elif (user_choice == "Stone" and comp_choice == "Scissors") or \
         (user_choice == "Paper" and comp_choice == "Stone") or \
         (user_choice == "Scissors" and comp_choice == "Paper"):
        print("Result: You Win")
    else:
        print("Result: Computer Wins")