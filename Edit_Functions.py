from Search_Functions import searchCatalog
import os

def editCatalog(catalog):
    # Adds or removes items from catalog based on user choice
    print("\nEnter 1 to add to the catalog,")
    print("Enter 2 to delete from the catalog, ")
    editType = input("Enter 3 to exit to edit menu: ")
    if editType == '1':
        addBook(catalog)
    elif editType == '2':
        deleteBook(catalog)
    elif editType == '3':
        print()
        return
    else:
        print("ERROR... input must be \"1\" or \"2\"")
        editCatalog(catalog)

def addBook(catalog):
    # Adds book information from user to catalog file & list
    
    # Loop to add as many books as user desires
    while True:
        # Get input from user
        title = input("\nEnter the title of the book: ")
        author = input("Enter the author of the book: ")
        pubDate = input("Enter the book's year of publication: ")
        while not pubDate.isnumeric() or len(pubDate) != 4:
            print("ERROR... please enter the 4-digit representation of the year: ")
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
            print("\nDo you wish to enter another book?")
            choice = input("Type 'Y' for yes or 'N' for no.")
            if choice.upper() == 'N':
                # User done; exits loop and therefore function
                print("Additions complete.\n")
                break
        else:
            # Does not add info to catalog; asks if user wishes to re-enter info
            print("\nDo you wish to correct this information?")
            choice = input("Type 'Y' for yes or 'N' for no.")
            if choice.upper() == 'N':
                # User done; prints message; exits loop and therefore function 
                print("Additions complete.\n")
                break

def deleteBook(catalog):
    # Deltes book information that user selects from catalog file & list
    # Open file
    openCatalog = open('catalog.txt', 'r')
    # Ask user for input
    print("\nSelect how to search for the item you wish to delete: ")
    # Search for item matching input
    searchType = '1'
    infoList, foundIt, searchType = searchCatalog(catalog)
    if searchType != '4':
        formatInfo(infoList)
        # Confirm information is correct
        infoCorrect = input("\nIs this the book you wish to remove (Y for yes, N for no)?")
        if infoCorrect.upper() == 'Y':
            # Information correct; open temporary file
            tempCat = open('temp_cat.txt', 'w')
            info = infoList[0] # Selects tuple from list
            lines = openCatalog.readlines() # Creates list of every line in file
            outerCount = 0 # Loop control variable
            newCatalog = []
            for outerCount in range((len(lines) // 4) + 1):
            # Creates new catalog with tuples of information, used to write 
                innerCount = 0 + (outerCount * 4)
                # used to select items from list to create tuple
                title = lines[innerCount] # title of book
                innerCount += 1
                author = lines[innerCount] # author of book
                innerCount += 1
                pubDate = lines[innerCount] # publication year of book
                innerCount += 1
                if innerCount != (len(lines)):
                # Adds <> as part of book information, unless eof reached
                    newLine = lines[innerCount] # Line in between books
                    innerCount += 1
                else:
                # At eof, gives last item empty string instead of <>
                    newLine = ''
                fileInfo = (title, author, pubDate, newLine)
                    # Tuple of book information, read from file
                newCatalog.append(fileInfo) # Add tuple to catalog used to write to new file
                outerCount += 1
            
            lastMatch = False # Indicates if item to be removed is last in file
            lastItem = newCatalog[len(newCatalog) - 1] # Finds last info in list
            if info[0] == (lastItem[0]).rstrip():
            # Item to be removed is last in file
                lastMatch = True

            # Loop to write other books to file
            count = 0
            newCount = 0
            for count in range(len(newCatalog)):
                
                book = newCatalog[count] # tuple of book information read from file

                if lastMatch == False:
                # Item removed is not last in list
                    if (book[0]).rstrip() != info[0]:
                    # Writes book to new file unless it is the one to be deleted
                        tempCat.write(book[0])
                        tempCat.write(book[1])
                        tempCat.write(book[2])
                        if book[3] != '':
                        # Writes <> if not eof
                            tempCat.write(book[3])
                else:
                # Item removed is last in list
                    if count != len(newCatalog) - 1:
                    # Writes everything but last book to new file
                        tempCat.write(book[0])
                        tempCat.write(book[1])
                        if count != len(newCatalog) - 2:
                        # Writes all data b/c not penultimate book in file
                            tempCat.write(book[2])
                            tempCat.write(book[3])
                    else:
                    # Only writes date of book; no newline character or <>
                        tempCat.write((book[2]).rstrip())
                    newCount += 1
                    
            # Close files
            openCatalog.close()
            tempCat.close()
            # Remove old file; rename new file
            os.remove('catalog.txt')
            os.rename('temp_cat.txt', 'catalog.txt')
            # Remove from catalog list
            count = 0
            for item in catalog:
                if info[0] == item[0] and info[1] == item[1] and info[2] == item[2]:
                    catalog.pop(count)
                count += 1
            # Print message
            print("Book removed from catalog")
        else:
            # Close files
            openCatalog.close()
            fixInfo = input("Do you wish select another book (Y for yes, N for no)?")
            if fixInfo.upper() == 'Y':
                deleteBook(catalog)
            else:
                return
            

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
