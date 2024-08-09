import random

while True:
    print("================================")
    print("Rock Paper Scissors")
    print("================================")
    print("1) ✊")
    print("2) ✋")
    print("3) ✌")
    player = int(input("Pick a number between 1 and 3: "))
    if player == 1:
        print("You chose: ✊")
    elif player == 2:
        print("You chose: ✋")
    elif player == 3:
        print("You chose: ✌")
    else:
        print("Invalid choice. Please select 1,2,3")
    computer = random.randint(1, 3)
    if computer == 1:
        print("CPU chose: ✊")
    elif computer == 2:
        print("CPU chose: ✋")
    elif computer == 3:
        print("CPU chose: ✌")
    if player == computer:
        print("It's a tie!")
    elif (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1): 
        print("CPU win")
    else:
        print("You win!")
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        break  
print("Thanks for playing! Have a great day!")
