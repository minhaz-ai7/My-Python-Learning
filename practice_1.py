import os
os.system('cls' if os.name == 'nt' else 'clear')

# food = {
#     "mango": 2.55,
#     "banana": 5.77,
#     "juice": 3.33,
#     "chips": 1.4
# }


# cart = []

# total = 0


# print("------------- MENU --------------")
# for key, value in food.items():
#     print(f"{key:10} :  ${value:.3f}")

# print("-----------------------------")

# while True:
#     food = input("select an item (q to quit): ").lower()
#     if food == "q" :
#         break



# import random

# low = 1 
# high = 100 

# number = random.randint(low,high)

# print(number)


#smart grade & class statistics system 

# import csv 

# def calculate_grade(avg):
#     if avg >= 90: return "A+"
#     elif avg >= 80: return "A"
#     elif avg >= 70: return "B"
#     else: return "F"


# def add_student_data():
#     Name = input("enter student name: ")
#     marks = []

#     for sub in ["Math" , "Physics" , "Chemistry" ]:
#         score = int(input(f"enter {sub} number: "))
#         marks.append(score)
        
        
#     Total = sum(marks)
#     Average = Total / len(marks)
    
#     return {
#         "Name" : Name ,
#         "Total" : Total,
#         "average" : round(Average , 2 ),
#         "Grade" : calculate_grade(Average)
#     }
        
        
        
# def save_and_show(Student):
#     with open ('class_data.csv' , 'a' , newline= '') as f :
#         writer = csv.DictWriter(f , fieldnames= ["Name" , "Total" , "average" , "Grade"])
#         f.seek(0,2)
        
#         if f.tell() == 0: writer.writeheader()
#         writer.writerow(Student)
        
        
#     print(f"{Student["Name"]} is data saved .. grade : {Student["Grade"]}")
    
            
# def main():
#     while True:
#         choice = input("\n1. add nw student\n2. see report \n3. quit \n fvt: ")
#         if choice == '1':
#             data  = add_student_data()
#             save_and_show(data)
#         elif choice == '2':
#             print("\n--- Student Report ---")
#             try:
#                 with open('class_data.csv', 'r') as f:
#                     reader = csv.DictReader(f)
#                     for row in reader:
#                         print(f"Name: {row['Name']}, Total: {row['Total']}, Grade: {row['Grade']}")
#             except FileNotFoundError:
#                 print("No data found!")
                
#         elif choice == '3':
#             break
#         else:
#             print("Invalid input!")
            
            
            
            
# main()



#2 


# def check_password_strength(password):
#     length_ok = len(password) >= 8
#     has_upper = any(char.isupper() for char in password)
#     has_loweer = any(char.islower() for char in password)
#     has_digit = any(char.isdigit() for char in password)
    
#     if length_ok and has_upper and has_loweer and has_digit:
#         return "Strong Password"
#     else:
#         return "weak password"
    
    
# user_pwd = input("enter password : ")
# result = check_password_strength(user_pwd)
# print(f"Your Password : {result}")




#3 project




# import csv

# def save_student(name , math , physics):
#     total = math + physics
#     avg = total / 2 
    
#     student_data = {
#         "Name" : name,
#         "Math" : int(math),
#         "Average" : avg
#     }
    
#     with open ('Class_data.csv' , 'a' , newline= '') as file:
#         writer = csv.DictWriter(file , fieldnames= ["Name" , "Math" , "Physics" , "Average"])
        
#         file.seek(0 , 2)
#         if file.tell() == 0 :
#          writer.writeheader()
        
#         writer.writerow(student_data)
        
#     print("Data saved")
    
    
# def read_student():
#         print("\n-----------class report-----------")
        
#         try:
#             with open('class_data.csv' , 'r' ) as file:
#                 reader = csv.DictReader(file)
#                 for row in reader:
#                     print(f"Name : {row['Name']} , average : {row['Average']}")
#         except FileNotFoundError :
#             print("Dont have data file ")
            
            
# while True:
#     choice = input("\n 1.Add new student \n 2. See report\n 3. Exit\n choice one: ")
#     if choice == '1':
#         name = input("name: ")
#         m = input("Math number: ")
#         p = input("physics number: ")        
#         save_student(name , m , p)
#     elif choice == '2':
#         read_student()
        
#     else:
#         break
                    



#Digital Libary system 


# library = {
#     "python basics" : 101 , 
#     "data science 101 " : 102,
#     "web devlopment" : 103 
# }


# book_ids = {101 , 102 ,103}

# def search_book(book_name):
#     if book_name.lower() in library:
#         book_id = library[book_name.lower()]
#         print(f"find this book ! is = {book_id}")
    
#     else:
#         print("dont found")
        
        
# def add_books(book_name , book_id):
#     if book_id in book_ids:
#         print("this code use for another book !")
        
#     else:
#         library[book_name.lower()] = book_id
#         book_ids(book_id)
#         print("add new books! ")
        

# while True:
#     print("/n------------library system----------------")
#     choice = input("1.search book\n 2. add books\n 3. Quite\n 4.choice: ")
    
#     if choice == 1 :
#         name = input("Books name: ")
#         search_book(name)
        
#     elif choice == 2 :
#         name = input("write book name: ")
#         bid = int(input('Books Id : '))
#         add_books(name,bid)
        
#     else:
#         break
        
        
# topics = ["Python" , "data science" , "getting to yes"]

# with open('my_notes.txt' , 'w' ) as f:
#     for x in topics:
#         f.write(x + "\n" )
    
# with open('my_notes.txt' , 'r') as f :
#     read = f.read()
#     print(read)




import json 



my_data = {
    "student_name": "Rahim",
    "id": 101,
    "skills": ["Python", "Data Analysis"],
    "is_graduated": False
}


with open("student.json" , 'w' ) as f:
    json.dump(my_data , f , indent= 4)
    print("ok")

with open("student.json" , 'r') as f:
    load_data = json.load(f)
    print("\n file theke pora data: ")
    print(f"name: {load_data['student_name']}")
    print(f"skills: {load_data['skills']}")










