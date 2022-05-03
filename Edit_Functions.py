from Search_Functions import searchCatalog

def editCatalog(catalog):
    # Adds or removes items from catalog based on user choice
    editType = int(input("Enter 1 to add to the catalog or 2 to delete from the catalog: "))
    if editType == 1:
        addBook(catalog)
    if editType == 2:
        deleteBook(catalog)

def addBook(catalog):
    # Adds book information from user to catalog file & list
    
    # Loop to add as many books as user desires
    while True:
        # Get input from user
        title = input("\Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        pubDate = input("Enter the book's year of publication: ")
        info = [(title, author, pubDate)]
        # Check if information is correct
        formatInfo(info)
        print("Is the above information correct?")
        check = input("Type 'Y' for yes or 'N' for no.")
        # Information correct; append to catalog file
        if check.upper() == 'Y':
            # Open file
            openCatalog = open('catalog.txt', 'a')
            # Write <> to file to ensure future searches run correctly
            openCatalog.write("\n<>\n")
            # Write information to file
            openCatalog.write(title + "\n")
            openCatalog.write(author + "\n")
            openCatalog.write(pubDate)
            # Close file
            openCatalog.close()
            # Append info to catalog list
            catalog.append(info)
            # Ask user if they wish to continue
            print("Book added to catalog.")
            print("\nDo you wish to enter other information?")
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
