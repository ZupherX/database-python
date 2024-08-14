def main():
  print("------------------------------------------------")
  
  task = input("What would you like to do? (Find Data (FD) - Write Data (WD) - Edit Data (ED) - Print Data (PD) - Clear Data (CD): ").lower()

  match(task):
    case "fd":
      findData()
    case "wd":
      writeData()
    case "ed":
      editData()
    case "pd":
      printData()
    case "cd":
      clearData()
    case _:
      print("Invalid Input.")
      main()


def findData():
  print("------------------------------------------------")

  dataTitle = input("Whats the title of the data you are finding? ")

  
  print("Opening Database...")


  with open("data.txt", "r") as file:

    print("Finding Data...")

    for line in file:

      print("Fetching Database...")
      
      title, data = line.split("-")

      if dataTitle.lower() == title.lower():
        print("Confirming Data...")
        print()
        print("Data:", data)
        main()
        return 0

    file.close()
        
    print()
    print("Couldn't find data.")
    main()

def writeData():
  print("------------------------------------------------")

  print("Opening Database...")

  dataTitle = input("Enter your new data title: ")
  dataData = input("Enter the data you want to save to that title: ")

  with open("data.txt", "r") as file: 

    print("Fetching Database...")

    for line in file:
      title, data = line.split("-")

      if title.lower() == dataTitle.lower():
        print("Title is already in use.")
        main()
        return 0
        
    file.close()
        
  with open("data.txt", "a") as file:
  
    print("Writing data...")

    file.write(dataTitle + "-" + dataData + "\n")

    file.close()
  
  main()

def editData():
  print("------------------------------------------------")

  oldTitle = input("Enter title of data to edit: ").lower()
  oldData = ""
  
  Lines = ""
  lineIndex = -1
  Found = False

  with open("data.txt", "r") as file:

    print("Fetching Data...")
    
    Lines = file.readlines()

    file.close()

  for index, line in enumerate(Lines):
    currentTitle, currentData = line.lower().split("-")
    
    if currentTitle == oldTitle:
      print("Checking Data...")
      oldData = currentData.capitalize()
      lineIndex = index
      Found = True

  if Found:
    newTitle = ""
    newData = ""

    toEdit = input("What would you like to change: (Title (T) - Data (D))").lower()

    if toEdit == "t":
      newTitle = input("Enter the new title: ").lower().capitalize()

      print("Modifying Data...")

      Lines[lineIndex] = newTitle + "-" + oldData + "\n"
    elif toEdit == "d":
      newData = input("Enter the new data: ")

      print("Modifying Data...")
      
      Lines[lineIndex] = oldTitle + "-" + newData + "\n"
  else:
    print("Couldn't find specific title.")
    main()
    return 0

  with open("data.txt", "w") as file:
    file.writelines(Lines)
    
    file.close()

  main()

def printData():
  print("------------------------------------------------")

  with open("data.txt", "r") as file:
    for line in file:
      print(line)

    file.close()

  main()

def clearData():
  print("------------------------------------------------")
  
  print("Clearing data...")

  with open("data.txt", "w") as file:
    file.write("")
  
    file.close()

  print("Cleared Data.")
  
  main()

main()
