# Program name: LibraryCatalog
# Author: Mary Krane
# Date: 03/18/2022
# Summary: Find and alter items in a list of books
# Variables:
#

from Search_Functions import titleSearch, authorSearch, pubDateSearch
catalogList = []

def main():
    housekeeping()
    choice = chooseFunction()
    if choice == 1:
        searchCatalog()
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

def searchCatalog():
    info = ""
    print("Enter 1 to search by title, ")
    print("Enter 2 to search by author, ")
    searchType = int(input("or 3 to search by publication date: "))
    if searchType == 1:
        info = titleSearch(catalogList)
    if searchType == 2:
        info = authorSearch(catalogList)
    if searchType == 3:
        info = pubDateSearch(catalogList)
    print(info)

main()
