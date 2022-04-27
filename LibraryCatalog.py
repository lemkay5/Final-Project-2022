# Program name: LibraryCatalog
# Author: Mary Krane
# Date: 03/18/2022
# Summary: Find and alter items in a list of books
# Variables:
#

from Search_Functions import searchCatalog, titleSearch, authorSearch, pubDateSearch
from Edit_Functions import editCatalog, addBook, deleteBook
catalogList = []

def main():
    housekeeping()
    choice = chooseFunction()
    if choice == 1:
        info, foundIt = searchCatalog(catalogList)
        if foundIt == True:
            formatInfo(info)
        if foundIt == False:
            print(info)
    if choice == 2:
        editCatalog()

def housekeeping():
    openCatalog = open('catalog.txt', 'r')
    newLine = ""
    count = 0
    while True:
        title = (openCatalog.readline()).rstrip('\n')
        author = (openCatalog.readline()).rstrip('\n')
        pubDate = (openCatalog.readline()).rstrip('\n')
        item = (title, author, pubDate)
        catalogList.append(item)
        count += 1
        newLine = openCatalog.readline()
        if newLine.rstrip('\n') != "<>":
            openCatalog.close()
            break
    return catalogList

def chooseFunction():
    choice = int(input("Enter 1 to search the catalog or 2 to edit it: "))
    return choice

def formatInfo(book):
    for item in book:
        print("\nTitle: " + item[0])
        print("Author: " + item[1])
        print("Year Published: " + item[2])
    
main()
