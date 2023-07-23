import time
import Functions as f
now = time.strftime("%H: %M - %b, %d")
print(now)

List = []
List = f.FileManage("Fetch", List)
while True:
    action = input("Type Add, Show, Edit, Complete, or Exit:  ")
    action = action.strip()  # Removes spaces
    action = action.upper()  # Formats input into simpler values

    if action.startswith("ADD"):  # Adds new entry to list
        Item = action[4:] + "\n"
        List.append(Item.capitalize())
        f.FileManage("Alter", List)
    elif action.startswith("SHOW"):  # Shows the entire list
        f.FileManage("Fetch", List)
        for index, item in enumerate(List):
            row = f"{index + 1}-{item}"
            print(row.strip("\n"))
    elif action.startswith("EDIT"):  # Changes specific index in list
        try:
            index = int(action[5:])
            index = index - 1
            new_item = input("Enter a new Value: ")
            List[index] = new_item.capitalize()
            f.FileManage("Alter", List)
        except ValueError:
            print("Value not recognised")
        except IndexError:
            print("Index not recognised")

    elif action.startswith("COMPLETE"):
        try:
            index = int(action[9:])
            List.pop(index - 1)
            f.FileManage("Alter", List)
        except ValueError:
            print("Value not recognised")
        except IndexError:
            print("Index not recognised")

    elif action.startswith("EXIT"):  # Exits the program
        break
    else:
        print("Command not recognised!")


print("GOODBYE!")