import random

def main():
    # choice of rock, paper, scissors
    user_choice = int(input("geef een nummer van 1 tot 3 (rock (1), paper(2) of scissor(3))"))
    choices = ["rock", "paper", "scissor"]
    # user choice
    user_choice -= 1
    user_choice_element = choices[user_choice]
    print('User:', user_choice_element, user_choice)
    # computer chooses
    computer_choice_element = random.choice(choices)
    # determine winner
    computer_choice = choices.index(computer_choice_element)    
    print('Computer:', computer_choice_element, computer_choice)

    # 1 > 3
    # 1 < 2
    # 2 < 3
    winner = "nobody"
    
    if user_choice == 0:
        if computer_choice == 2:
            winner = "User"
        elif computer_choice == 1:
            winner = "Computer"


    print("the winner is", winner)

    # print winner

main()