import random

user_score = 0
computer_score = 0

def play_game():
    global user_score , computer_score

    choices = ["rock","paper","scissors"]
    user_choice = input("Choose rock,paper or scissors:").lower()
    computer_choice = random.choice(choices)

    if user_choice not in choices:
        print("Invalid choice.\n Please choose rock, paper and scissors.")
        return

    print("\nYou chose:", user_choice)
    print("\nComputer chose:", computer_choice)

    if user_choice == computer_choice:
        print("\nIt's a tie!\n")
        
    elif user_choice == "rock" and computer_choice == "scissors":
        print("\nYou win!\n")
        user_score+=1
        
    elif user_choice == "paper" and computer_choice == "rock":
        print("\nYou win!\n")
        user_score+=1
        
    elif user_choice == "scissors" and computer_choice == "paper":
        print("\nYou win!\n")
        user_score+=1
        
    else:
        print("\nComputer wins!\n")
        computer_score+=1
        
    return user_score , computer_score

while True:
    play_game()

    play_again= input("\nDo you want to play another round?(yes/no):").lower()
    if play_again != "yes":
        break

print("\n Game over!!")
print("\nYour score:", user_score)
print("\nComputer score:", computer_score)