def titleSearch(catalog):
    count = 0
    matches = []
    foundIt = False
    notFound = "Item not in catalog."
    searchKey = input("Enter the title of the book: ")
    while count < len(catalog):
        info = catalog[count]
        if searchKey in info[0]:
            foundIt = True
            matches.append(info)
        count += 1
    if foundIt == False:
        return notFound
    else:
        return matches

def authorSearch(catalog):
    count = 0
    matches = []
    foundIt = False
    notFound = "Item not in catalog."
    searchKey = input("Enter the author of the book: ")
    while count < len(catalog):
        info = catalog[count]
        if searchKey in info[1]:
            foundIt = True
            matches.append(info)
        count += 1
    if foundIt == False:
        return notFound
    else:
        return matches

def pubDateSearch(catalog):
    count = 0
    matches = []
    foundIt = False
    notFound = "Item not in catalog."
    lowerDate = int(input("Enter the earliest date: "))
    upperDate = int(input("Enter the latest date: "))
    while count < len(catalog):
        info = catalog[count]
        date = int(info[2])
        if lowerDate < date < upperDate:
            foundIt = True
            matches.append(info)
        count += 1
    if foundIt == False:
        return notFound
    else:
        return matches
