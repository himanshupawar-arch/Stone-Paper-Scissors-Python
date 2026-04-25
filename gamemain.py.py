from game_pkg import logic

def main():
    # Infinite loop for the game menu
    while True:
        print("\n Stone Paper Scissors ")
        print("1. Play Game")
        print("2. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            logic.play_round()
        elif choice == '2':
            print("Exiting game. See you next time")
            break
        else:
            print("Invalid input. Please enter 1 or 2.")

if __name__ == "__main__":
    main()