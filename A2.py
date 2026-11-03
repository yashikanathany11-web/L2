import random
while True:
    u_a = input("Enter a choice (rock, paper, scissors): ")
    p_a = ["rock", "paper", "scissors"]
    c_a = random.choice(p_a)
    print(f"\nYou chose {u_a}, computer chose {c_a}. \n")

    if u_a == c_a:
        print(f"BOTH PLAYERS SELECTED {u_a}. Its a tie!")
    elif u_a == "rock":
        if c_a == "scissors":
            print("Rock smashed the scissors! You win!")
        else:
            print("Paper covers rock! YOU LOSE!")
    elif u_a == "paper":
        if c_a== "rock":
            print("Paper covers rock! YOU WIN!")
        else:
            print("Scissors cut paper! YOU LOSE.")
    elif u_a == "scissors":
        if c_a == "paper":
            print("Scissors cuts paper! YOU WIN!")
        else:
            print("Rock smashed the scissors! YOU LOSE.")

    play_a = input("PLAY AGAIN? (y/n): ")
    if play_a != "y":
        break
    

