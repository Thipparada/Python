import random
def PaoYingChup():
    score = 0
    print("Let's play pao-ying-chup game!")
    while True:
        player = input("Rock ,Scissors ,or Paper: ")
        player = player.lower()
        choice = ["rock", "paper", "scissors"]
        com = random.choice(choice)
        player = player.lower()
        if player in choice:
            if player == "quit":
                print("See you later!")
                break
            elif player == com :
                print("Square game!")
            elif player == "rock" and com == "scissors":
                print("Yeah! you win")
                score +=1
            elif player == "scissors" and com == "paper":
                print("Yeah! you win")
                score +=1
            elif player == "paper" and com == "rock":
                print("Yeah! you win")
                score +=1    
            else:
                print("Sorry you lose")
        elif player == 'quit':
            print("See you later!")
            break
        else:
            print("Your input is not correct pleas try again")
    print("Your score is",score)
