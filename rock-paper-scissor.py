import random

def game(comp, you):
    if comp == you:
        return None 
    elif comp == 0:
        if you == 1:
            return True
        elif you == 2:
            return False  
    elif comp == 1:
        if you == 0:
            return False
        elif you == 2:
            return True 
    elif comp == 2:
        if you == 0:
            return True
        elif you == 1:
            return False   

while True:
    print("Comp turn: scissor (0), rock (1), paper (2)")
    comp = random.randint(0, 2)
    you = int(input("Your turn: scissor (0), rock (1), paper (2) -> "))  
    result = game(comp, you)

    print(f"The computer is {comp}")
    print(f"You are {you}")

    if result == None:
        print("It's a draw!")
    elif result == True:
        print("You win!")
    else:
        print("Computer wins!")

    play_again = input("Do you want to play again? (y/n)").lower()
    if play_again == "n":
        break
print("Thanks for playing!")

