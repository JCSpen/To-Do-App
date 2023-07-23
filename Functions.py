def FileManage(cmd, contents):
    """ Performs both read and write in the same method"""
    match cmd:
        case "Fetch":
            with open("Data.txt", "r") as file:
                return file.readlines()
        case "Alter":
            with open("Data.txt", "w") as file:
                file.writelines(contents)
            return "List updated successfully"