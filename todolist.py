file = open("list.txt", "a+")
menu = 0
procData = []

def represent(name):
    rawData = file.readlines()

    for line in rawData:
        procData.append(line.split())

    names = [item[0] for item in procData]
    index = names.index(name)
    print(names[index] + ":\n\n")

    for x in range(len(procData[index]):
        print((x + 1) + ") " + )



def dispLists():
    return False






while menu == 0:
    userinput = input(
        "Would you like to create a new to-do list or modify an existing one?\n\n1) Create a new list"
        "\n2) Modify or view an existing list\n\n")

    if userinput == "1":
        menu = 1
    elif userinput == "2":
        menu = 2
    else:
        print("Invalid input! Please type the digit(s) of the corresponding option.")
        break

while menu == 1:
    listName = input("Enter the name for your new list:\n")
    file.write(listName)
    print("To-do list " + listName + " has been successfully created.")
    menu = 2

while menu == 2:
    currentList = "NONE"

    if listName:
        currentList = listName
        listName = False

    input = input(
        "Currently selected list: " + currentList + "\n\n1) View or modify currently selected list"
                                                    "\n2) Select another list\n3) Return to main menu\n\n")

    if input == "1":
        print("Current items in " + currentList + "\n")
        represent(currentList)
    elif input == "2":
        print("tba")
    elif input == "3":
        menu = 0
    else:
        print("Invalid input! Please type the digit(s) of the corresponding option.")
        menu = 0
