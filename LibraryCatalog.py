# Program name: LibraryCatalog
# Author: Mary Krane
# Date: 03/18/2022
# Summary: Find and alter items in a list of books
# Variables:
#

# import functions
from Search_Functions import searchCatalog 
from Edit_Functions import editCatalog
catalogList = [] # initialize list of books

def main():
    housekeeping()
    choice = chooseFunction()
    # Run search or edit functions depending on user choice
    if choice == 1:
        info, foundIt = searchCatalog(catalogList) # search results & flag
        if foundIt == True:
            formatInfo(info)
        if foundIt == False:
            print(info)
    if choice == 2:
        editCatalog(catalogList)

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
    choice = int(input("Enter 1 to search the catalog or 2 to edit it: "))
    return choice

def formatInfo(book):
    # Formats and prints book information
    for item in book:
        print("\nTitle: " + item[0])
        print("Author: " + item[1])
        print("Year Published: " + item[2])
    
main()
