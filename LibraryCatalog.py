# Program name: LibraryCatalog
# Author: Mary Krane
# Date: 03/18/2022
# Summary: Find and alter items in a list of books

# import functions
from Search_Functions import searchCatalog 
from Edit_Functions import editCatalog
catalogList = [] # initialize list of books

def main():
    housekeeping()
    choice = chooseFunction()
    while choice != '3':
        # Run search or edit functions depending on user choice
        if choice == '1':
            # Search as many times as the user wishes
            searchType = '1'
            while searchType != '4':
                # User has made a search
                info, foundIt, searchType = searchCatalog(catalogList)
                # search results, flag, and whether to search again

                if foundIt == True:
                    # Match found, prints matches
                    print("\nResults:")
                    formatInfo(info)
                if foundIt == False:
                    # No matches, prints message returned by function
                    print(info)
        elif choice == '2':
            # Edits catalog how user wishes
            editCatalog(catalogList)
        else:
            # Input does not match choices
            print("ERROR... input must be \"1\", \"2\", or \"3\"")
        # Ask user to choose function again
        choice = chooseFunction()
    print("\nEnd of program.")

def housekeeping():
    # Create list of tuples containing the data of the books
    openCatalog = open('catalog.txt', 'r') # opens file
    newLine = "" # initialize loop control
    
    # Loop to add item to list of books
    while True:
        # Create tuple containing title, author, and publication date
        title = (openCatalog.readline()).rstrip('\n')
        author = (openCatalog.readline()).rstrip('\n')
        pubDate = (openCatalog.readline()).rstrip('\n')
        item = (title, author, pubDate)

        # Add tuple to list of books
        catalogList.append(item)

        # Read next item
        newLine = openCatalog.readline()

        # Exits loop if no further items
        if newLine.rstrip('\n') != "<>":
            openCatalog.close()
            break

    # returns list of books
    return catalogList

def chooseFunction():
    # User chooses whether to search or edit the catalog
    choice = input("Enter 1 to search catalog, 2 to edit it, or 3 to quit: ")
    return choice

def formatInfo(book):
    # Formats and prints book information
    for item in book:
        print("Title: " + item[0])
        print("Author: " + item[1])
        print("Year Published: " + item[2] + '\n')
    
main()
