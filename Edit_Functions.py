from Search_Functions import searchCatalog
import os

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
            print("\nDo you wish to enter another book?")
            choice = input("Type 'Y' for yes or 'N' for no.")
            if choice.upper() == 'N':
                # User done; exits loop and therefore function
                print("Additions complete.")
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
    # Open file
    openCatalog = open('catalog.txt', 'r')
    # Ask user for input
    print("\nSelect how to search for the item you wish to delete: ")
    # Search for item matching input
    searchType = '1'
    infoList, foundIt, searchType = searchCatalog(catalog)
    #while infoList == "error":
        #info, foundIt, searchType = searchCatalog(catalog)
    print(searchType)
    if searchType != '4':
        formatInfo(infoList)
        # Confirm information is correct
        infoCorrect = input("\nIs this the book you wish to remove (Y for yes, N for no)?")
        if infoCorrect.upper() == 'Y':
            # Information correct; open temporary file
            tempCat = open('temp_cat.txt', 'w')
            info = infoList[0] # Selects tuple from list
            # Read first line of file
            line = (openCatalog.readline()).rstrip()
            while line != '':
                # Loop write other books to new file
                if info[0] == line:
                    line = (openCatalog.readline()).rstrip()
                    line = (openCatalog.readline()).rstrip()
                    line = (openCatalog.readline()).rstrip()
                    line = (openCatalog.readline()).rstrip()
                tempCat.write(line)
                line = (openCatalog.readline()).rstrip()
                if line != '':
                    tempCat.write('\n')
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
            tempCat.close()

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
