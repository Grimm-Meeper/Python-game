Places = []
People = []
def do_something():
    action = input("What do you want to do?")
    if action == "ADD_CHAR":
        People.append(input("Who to add?"))
    elif action == "ADD_PLACE":
        Places.append(input("Where to add?"))
    else:
        print("Please try again")
        do_something()
    print(f"People: {People}, places: {Places}.")
    if input("Add aonther?(y/n)") == "y":
        do_something()
    else:
        print("Goodbye.")
        print(f"People: {People}, places: {Places}.")
do_something()