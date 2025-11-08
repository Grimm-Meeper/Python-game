Places = []
People = []
def decide_something():
    action = input("What do you want to do?")
    if action == "ADD_CHAR":
        People.append(input("Who to add?"))
        repet()
    elif action == "ADD_PLACE":
        Places.append(input("Where to add?"))
        repet()
    else:
        print("Please try again")
        decide_something()

def repet():
    print(f"People: {People}, places: {Places}.")
    if input("Add aonther?(y/n)") == "y":
        decide_something()
    else:
        print(f"People: {People}, places: {Places}.")
        print("Goodbye.")

decide_something()