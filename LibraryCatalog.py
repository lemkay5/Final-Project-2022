# Program name: LibraryCatalog
# Author: Mary Krane
# Date: 03/18/2022
# Summary: Find and alter items in a list of books
# Variables:
#   

def main():
    title, author, pubDate, nextLine = getInfo()
    print(title, author, pubDate, nextLine)
    while nextLine.rstrip('\n') == "<>":
        title, author, pubDate, nextLine = getInfo()
        print(title, author, pubDate, nextLine)

        
    print("End of program")

def getInfo():
    openCatalog = open('catalog.txt', 'r')
    title = openCatalog.readline()
    author = openCatalog.readline()
    pubDate = openCatalog.readline()
    nextLine = openCatalog.readline()
    return title, author, pubDate, nextLine
    
main()
