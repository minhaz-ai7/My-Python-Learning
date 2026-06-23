import random 
import string

def generate_password():
    print("strong password generator")
    
    while True:
        try:
            length = int(input("how many wor in password.? (6-20):"))
            if  6 <= length <= 20 :
                break 
            else:
                print("enter 6 - 20  ")
                
        except ValueError:
            print("Invalid ")
            
    include_numbers = input("number thakbe.? (yes / no )").lower() == "yes"
    include_symbols = input("symbols thakbe.? (!@#$%^ etc ) (yes?no )").lower()== "yes"
        
    characters = string.ascii_letters
        
    if include_numbers :
            characters += string.digits
        
    if include_symbols:
            characters += "!@#$%^&*()_+-=[]{}|;:,.<>?"
         
    password =  ''.join(random.choice(characters) for i in range(length)) 
        
    print(f"\n your generator password: ")
    print(f"{password}")
    print(f"length: {length} characters ")
            

if __name__ == "__main__":
    generate_password()

