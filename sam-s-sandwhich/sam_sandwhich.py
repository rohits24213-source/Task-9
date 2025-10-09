def bread_selection ():
    bread_list = ["White","Brown","Italian","Granary"]
    count = 0
    print("We have the follwing bread")
    while count < len(bread_list):
        print(count+1," ",bread_list[count])
        count +=1
    try:
        bread_selection = int(input("Select, which bread you like to have? Enter the amount:"))-1
        if 0 <= bread_selection < len(bread_list):
            return bread_list[bread_selection] #it will return back to the string
        else:
            print("Invalid selection! Please enter the invalid value")
            return None
    except ValueError:
        print("Invalid input. Please enter a number")
        return None
    
def choose_meat():
    meat_list = ["Tuna, Beef, Chicken, No meat"]
    count = 0
    print("we have the following meat")
    while count < len(meat_list):
        print(count+1," ", meat_list[count])
        count +=1
    try:
        choose_meat = int(input("select which meat you like to have? Enter the amount:"))-1
        if 0 <= choose_meat < len(meat_list):
          return meat_list[choose_meat]
        else:
         print("Invalid selection! please enter the invlid value")
         return None
    except ValueError:
        print("Invalid input. please enter a number")
        return None
    
def choose_cheese():
    cheese_list = ["Cheddar, Feta, Creame Cheese, Mozzarella"]
    count = 0
    print("we have the following Cheese")
    while count < len(cheese_list):
        print(count+1," ", choose_cheese[count])
        count +=1
    try:
        choose_cheese= int(input("select which Cheese you like to have? Enter the amount:"))-1
        if 0 <= choose_cheese < len(cheese_list):
          return cheese_list[choose_cheese]
        else:
         print("Invalid selection! please enter the invlid value")
         return None
    except ValueError:
        print("Invalid input. please enter a number")
        return None
    