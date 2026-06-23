""" ROCK PAPER SCISSORS GAME """

import random 

def rock_paper_scissors():
    print("welcome to rock paper scissors ! ")
    print("rules : rock , pepar , scissors (any one choice)")
    
    choices = ['Rock' , 'Paper' , 'Scissors']
    
    while True:
        user_choices = input("\n Your choices (Rock , Paper , Scissors): ").title().strip()
        
        if user_choices not in choices:
            print("invaild input ")
            continue
        
        computer_choice = random.choice(choices)
        
        print(f"your choice : {user_choices}")
        print(f"computer choices: {computer_choice}")
        
        if user_choices == computer_choice:
            print("Draw , again play")
            
        elif (
            (user_choices == "Rock" and computer_choice == "Scissors") or 
            (user_choices == "Paper" and computer_choice == "Rock") or
            (user_choices == "Scissors" and computer_choice == "Paper")
        ):
            print('you win')
            
        else:
            print("computer win ")
            
            
        play_again = input("\nAgain play .? (Yes / No)").title().strip()
        if play_again != "Yes":
             print("TnQ for playing")
             break
            
            
if __name__ == "__main__":
    rock_paper_scissors()
            
            