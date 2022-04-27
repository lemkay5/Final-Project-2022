def editCatalog():
    editType = int(input("Enter 1 to add to the catalog or 2 to delete from the catalog: "))
    if editType == 1:
        addBook()
    if editType == 2:
        deleteBook()

def addBook():
    openCatalog = open('catalog.txt', 'a')
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    pubDate = input("Enter the book's year of publication: ")
    openCatalog.write("\n<>\n")
    openCatalog.write(title + "\n")
    openCatalog.write(author + "\n")
    openCatalog.write(pubDate)
    print("Book added")
    openCatalog.close()

def deleteBook():
    openCatalog = open('catalog.txt', 'w')
    openCatalog.close()
