Places = []
People = []
lists = [People, Places]
def pick_action():
    action = input("What do you want to do?").lower()
    if action == "add":
        Add()
        repet()
    elif action == "remove":
        Remove()
    else:
        print("Please try again")
        pick_action()

def Add():
    action = input("What to add?").lower()
    if action == "place":
        Places.append(input("Where?"))
    elif action == "person":
        People.append(input("Who?"))
    elif action == "cansil":
        print("Okay")
        repet()
    else:
        print("Try again")
        Add()

def Remove():
    lists = [People, Places]
    print(lists)
    action = input("What to remove?")
    print(action)
    for inner in lists:
        if action in inner:
            inner.remove(action)
            repet()
    if action == "cansil":
        print("Okay")
        repet()
    else:
        print("Try again")
        Remove()

def repet():
    print(f"People: {People}, places: {Places}.")
    if input("Do something else?(y/n)").lower() == "y":
        pick_action()
    else:
        print(f"People: {People}, places: {Places}.")
        print("Goodbye.")

pick_action()