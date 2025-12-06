things = {
    "people": [],
    "places": [],
    "items": [],
    "months": []
}
Year = None
Season = ""

def pick_action():
    action = input("What do you want to do?").lower()
    if action == "add":
        Add()
    elif action == "remove":
        Remove()
    elif action == "time":
        time()
    else:
        print("Please try again")
        pick_action()

def Add():
    action = input("What to add?").lower()
    if action == "place":
        things["places"].append(input("Where?"))
        repet()
    elif action == "person":
        things["people"].append(input("Who?"))
        repet()
    elif action == "item":
        things["items"].append(input("What?"))
        repet()
    elif action == "month":
        things["months"].append(input("When?"))
        repet()
    elif action == "cansil":
        print("Okay")
        repet()
    else:
        print("Try again")
        Add()

def Remove():
    Show_Vars()
    action = input("What to remove?")
    print(f"removing {action}")
    for key, lst in things.items():
        if not things[key] == []:
            for item in lst:
              if action == item:
                  lst.remove(item)
                  repet()
                  return
    if action == "cansil":
        print("Okay")
        repet()
    else:
        print("Try again")
        Remove()

def time():
    action = (input("What do you want to do with time?")).lower()
    if action == "set":
        action = input("What to set?").lower()
        if action == "year":
            action = input("What to set the year to?")
            try:
                Year = int(action)
                repet()
            except ValueError:
                print("Invalid year")
                repet()
                pass
        elif action == "season":
            Season = input("What season?")
            repet()
        elif action == "cansil":
            print("okay.")
            repet()
        else:
            print("try again.")
            time()
    elif action == "cansil":
            print("okay.")
            repet()
    else:
        print("try again.")
        time()

def Show_Vars():
    print()
    for key, lst in things.items():
        if not things[key] == []:
            print(f"--- {key} ---")
            for item in lst:
              print(item)
    if not Year == None:
        print(f"Year: {Year}")
    if not Season == "":
        print(f"Season: {Season}")
    print()

def repet():
    Show_Vars()
    if input("Do something else?(y/n)").lower() == "y":
        pick_action()
    else:
        Show_Vars()
        print("Goodbye.")

pick_action()