things = {
    "people": {},
    "places": {},
    "items": {},
    "months": {}
}
Year = None
Season = ""
show = 1
def pick_action():
    action = input("What do you want to do? ").lower()
    if action == "add":
        Add()
    elif action == "remove":
        Remove()
    elif action == "time":
        time()
    elif action == "attributes":
        attributes()
    else:
        print("Please try again")
        pick_action()

def Add():
    action = input("What to add? ").lower()
    if action == "place":
        things["places"][input("Where? ")] = []
        repet()
    elif action == "person":
        things["people"][input("Who? ")] = []
        repet()
    elif action == "item" or action == "thing":
        things["items"][input("What? ")] = []
        repet()
    elif action == "month":
        things["months"][input("When? ")] = []
        repet()
    elif action == "cansil":
        print("Okay")
        repet()
    else:
        print("Try again")
        Add()

def Remove():
    Show_Vars(0)
    action = input("What to remove? ")
    print(f"removing {action}")
    for outer_key, inner_dict in things.items():
     if action in inner_dict:
        del inner_dict[action]
        print(f"Removed '{action}' from {outer_key}")
        repet()
        return
    if action == "cansil":
        print("Okay")
        repet()
    else:
        print("Deletion faled, please try again.")
        Remove()

def time():
    action = (input("What do you want to do with time? ")).lower()
    if action == "set":
        action = input("What to set? ").lower()
        if action == "year":
            action = input("What to set the year to? ")
            try:
                Year = int(action)
                repet()
            except ValueError:
                print("Invalid year, please try again.")
                time()
                pass
        elif action == "season":
            Season = input("What season? ")
            repet()
        elif action == "cansil":
            print("okay.")
            repet()
        else:
            print("Invalid set, please try again.")
            time()
    elif action == "cansil":
            print("okay.")
            repet()
    else:
        print("Invalid command, please try again.")
        time()

def attributes():
    action = input("What to do with them? ").lower()
    if action == "show":
        Show_Vars(1)
        repet()
    elif action == "add":
        Show_Vars(0)
        action = input("What to add to? ")
        for outer_key, inner_dict in things.items():
            if action in inner_dict:
                inner_dict[action].append(input("What to add? "))
                print("Added sucsefully")
                repet()
                return
    elif action == "cansil":
        print("Okay.")
        repet()
    else:
        print("Invalid command please try again.")
        attributes()

def Show_Vars(show_attributes):
    global show
    print()
    for type, items in things.items():
        if not things[type] == {}:
            print(f"--- {type} ---")
            for item, atribute in items.items():
              print(item)
              if show_attributes == 1:
                    for value in atribute:
                        print(f"   {value}")
                        show = 0

    if not Year == None:
        print(f"Year: {Year}")
    if not Season == "":
        print(f"Season: {Season}")
    print()

def repet():
    global show
    if show == 1:
        Show_Vars(0)
    show = 1
    if input("Do something else?(y/n) ").lower() == "y":
        pick_action()
    else:
        Show_Vars(1)
        print("Goodbye.")

pick_action()