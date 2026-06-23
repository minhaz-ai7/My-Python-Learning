import random 

def number_guessing_game():
    print("🎮 Welcome to Number Guessing Game!")
    print("1 to 100 any number guess ")
    
    secret_number = random.randint(1,100)
    
    attempts = 0
    max_attempts = 10 
    
    while True:
        try:
            guess = int(input("\nYour guess : "))
            attempts += 1 
            
            if guess == secret_number:
                print(f"congratulation {attempts} is correct ")
                break
            
            elif guess < secret_number:
                print("too Low !")
                
            else:
                print("too high ! guess low number !")
                
            
            if attempts >= max_attempts:
                print(f"Game over ⚔️ , correct is {secret_number}")
                break
                
        except ValueError:
            print(f"invaild input 🤷‍♂️ Try Again! ")
            continue
        
        
if __name__ == "__main__":
    number_guessing_game()
        
