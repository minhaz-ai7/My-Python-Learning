import csv 

def add_expeness(file_name):
    print("\n--- add new expense ---")
    
    item = input("what did you buy .? ")
    amount = input("how much.?")
    category = input("whice category [ food , travel , shopping]")
    
    expense = {
        "item" : item,
        "amount" : amount,
        "category" : category
        }
    
    with open (file_name , 'a' , newline = "") as file:
        fieldnames = ["Item", "Amount", "Category"]
        writer = csv.DictWriter(file , fieldnames= fieldnames )
        
        file.seek(0,2)
        if file.tell() == 0:
            writer.writeheader
            
        writer.writerow(expense)
        
        print("all expense done ")
        
        
    
   