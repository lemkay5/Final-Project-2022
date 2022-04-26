# Program name: LibraryCatalog
# Author: Mary Krane
# Date: 03/18/2022
# Summary: Find and alter items in a list of books
# Variables:
#

catalogList = []

def main():
    housekeeping()
    print(catalogList)
    
    

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
    
main()
