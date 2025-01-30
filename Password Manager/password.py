
def view ():
    pass
def add ():
    pass
def remove ():
    pass
def update ():
    pass

while True:
    password = input("Enter Your Options (View / Add / Remove / Update) Or Press Q to quit :").lower()
    if password == "Q":
        break
    elif password == "view":
        print("View")
    elif password == "add":
        print("Add")
    elif password == "remove":
        print("Remove")
    elif password == "update":
        print("Update")
    else:
        print("Invalid Input")