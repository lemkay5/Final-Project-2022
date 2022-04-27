def searchCatalog(catalog):
    info = ""
    print("\nEnter 1 to search by title, ")
    print("Enter 2 to search by author, ")
    searchType = int(input("or 3 to search by publication date: "))
    if searchType == 1:
        info, foundIt = titleSearch(catalog)
    if searchType == 2:
        info, foundIt = authorSearch(catalog)
    if searchType == 3:
        info, foundIt = pubDateSearch(catalog)
        
    return info, foundIt

def titleSearch(catalog):
    count = 0
    matches = []
    foundIt = False
    notFound = "Item not in catalog."
    searchKey = input("\nEnter the title of the book: ")
    while count < len(catalog):
        info = catalog[count]
        if searchKey in info[0]:
            foundIt = True
            matches.append(info)
        count += 1
    if foundIt == False:
        return notFound, False
    else:
        return matches, True

def authorSearch(catalog):
    count = 0
    matches = []
    foundIt = False
    notFound = "Item not in catalog."
    searchKey = input("\nEnter the author of the book: ")
    while count < len(catalog):
        info = catalog[count]
        if searchKey in info[1]:
            foundIt = True
            matches.append(info)
        count += 1
    if foundIt == False:
        return notFound, False
    else:
        return matches, True

def pubDateSearch(catalog):
    count = 0
    matches = []
    foundIt = False
    notFound = "Item not in catalog."
    lowerDate = int(input("\nEnter the earliest date: "))
    upperDate = int(input("Enter the latest date: "))
    while count < len(catalog):
        info = catalog[count]
        date = int(info[2])
        if lowerDate < date < upperDate:
            foundIt = True
            matches.append(info)
        count += 1
    if foundIt == False:
        return notFound, False
    else:
        return matches, True
