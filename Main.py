Places = []
People = []
def pick_action():
    action = input("What do you want to do?").lower()
    if action == "add":
        Add_something()
        repet()
    else:
        print("Please try again")
        pick_action()

def Add_something():
    action = input("What to add?").lower()
    if action == "place":
        Places.append(input("Where?"))
    elif action == "person":
        People.append(input("Who?"))
    else:
        print("Try again")
        Add_something()


def repet():
    print(f"People: {People}, places: {Places}.")
    if input("Add aonther?(y/n)").lower() == "y":
        pick_action()
    else:
        print(f"People: {People}, places: {Places}.")
        print("Goodbye.")

pick_action()