from Search_Functions import searchCatalog

def editCatalog(catalog):
    # Adds or removes items from catalog based on user choice
    editType = int(input("\nEnter 1 to add to the catalog or 2 to delete from the catalog: "))
    if editType == 1:
        addBook(catalog)
    if editType == 2:
        deleteBook(catalog)

def addBook(catalog):
    # Adds book information from user to catalog file & list
    
    # Loop to add as many books as user desires
    while True:
        # Get input from user
        title = input("\nEnter the title of the book: ")
        author = input("Enter the author of the book: ")
        pubDate = input("Enter the book's year of publication: ")
        info = [(title, author, pubDate)]
        # Check if information is correct
        formatInfo(info)
        print("Is the above information correct?")
        check = input("Type 'Y' for yes or 'N' for no.")
        if check.upper() == 'Y':
            # Information correct; check if any items in file
            openCatalog = open('catalog.txt', 'r')
            # Check if anything written in file
            firstLine = (openCatalog.readline()).rstrip()
            # Write information to file
            writeToFile(title, author, pubDate, catalog, firstLine)
            print("Do you wish to enter another book?")
            choice = input("Type 'Y' for yes or 'N' for no.")
            if choice.upper() == 'N':
                # User done; exits loop and therefore function
                print("Additions complete.")
                break
        else:
            # Does not add info to catalog; asks if user wishes to re-enter info
            print("Do you wish to correct this information?")
            choice = input("Type 'Y' for yes or 'N' for no.")
            if choice.upper() == 'N':
                # User done; prints message; exits loop and therefore function 
                print("Additions complete.")
                break

def deleteBook(catalog):
    print(catalog)
    openCatalog = open('catalog.txt', 'w')
    print("Select how to search for the item you wish to delete: ")
    info, foundIt = searchCatalog(catalog)
    formatInfo(info)
    print("Is this the book you wish to remove?")
    #formatInfo(info)
    openCatalog.close()

def formatInfo(book):
    # Formats and prints book information
    for item in book:
        print("\nTitle: " + item[0])
        print("Author: " + item[1])
        print("Year Published: " + item[2])

def writeToFile(title, author, pubDate, catalog, firstLine):
        # Open file
        openCatalog = open('catalog.txt', 'a')
        # Write <> if not first in file
        if firstLine != '':
            openCatalog.write("\n<>\n")
        # Remove empty tuple if no items in file when catalog created
        else:
            catalog.pop(0)
        openCatalog.write(title + "\n")
        openCatalog.write(author + "\n")
        openCatalog.write(pubDate)
        # Close file
        openCatalog.close()
        # Append info to catalog list
        catalog.append((title, author, pubDate))
        # Ask user if they wish to continue
        print("Book added to catalog.")
