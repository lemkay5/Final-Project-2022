def searchCatalog(catalog):
    # Searches catalog and retuns items found or message if not found
    
    info = "" # initializes variable to contain book information

    # Ask user for type of search
    print("\nEnter 1 to search by title, ")
    print("Enter 2 to search by author, ")
    searchType = int(input("Enter 3 to search by publication date: "))
    
    # Search based on user choice
    if searchType == 1:
        info, foundIt = titleSearch(catalog) # search results & flag
    if searchType == 2:
        info, foundIt = authorSearch(catalog) # search results & flag
    if searchType == 3:
        info, foundIt = pubDateSearch(catalog)# search results & flag
    return info, foundIt

def titleSearch(catalog):
    # Creates and returns list of tuples containing book
    # information for titles matching the user's search

    # Initialize variables
    count = 0 # loop control variable
    matches = [] # list of matches in catalog
    foundIt = False # flag indicating search success
    notFound = "Item not in catalog." # returned if no items match search

    # Get user input for search
    searchKey = input("\nEnter the title of the book: ")

    # Loop to check list of book information for user input
    while count < len(catalog):
        info = catalog[count]
        if searchKey in info[0]:
            # Match found; change flag and add to list of matches
            foundIt = True
            matches.append(info)
        count += 1
    if foundIt == False:
        # No matches; return message and flag
        return notFound, False
    else:
        # Return matches and flag
        return matches, True

def authorSearch(catalog):
    # Creates and returns list of tuples containing book
    # information for authors matching the user's search

    # Initialize variables
    count = 0 # Loop control variable
    matches = [] # List of matches in catalog
    foundIt = False # Flag indicating search successs
    notFound = "Item not in catalog." # Returned if no items match search

    # Get user input for search
    searchKey = input("\nEnter the author of the book: ")

    # Loop to check list of book information for user input
    while count < len(catalog):
        info = catalog[count]
        if searchKey in info[1]:
            # Match found, change flag and add to list of matches
            foundIt = True
            matches.append(info)
        count += 1
    if foundIt == False:
        # No matches; return message and flag
        return notFound, False
    else:
        # Return matches and flag
        return matches, True

def pubDateSearch(catalog):
    # Creates and returns list of tuples containing book
    # information for publication years matching the user's search
    count = 0 # Loop control variable
    matches = [] # List of matches in catalog
    foundIt = False # Flag indicating search successs
    notFound = "Item not in catalog." # Returned if no items match search

    # Get user input (earliest and latest dates) for search
    lowerDate = int(input("\nEnter the earliest date: "))
    upperDate = int(input("Enter the latest date: "))

    # Loop to check list of book information for user input
    while count < len(catalog):
        info = catalog[count]
        date = int(info[2])
        if lowerDate <= date <= upperDate:
            # Match found, change flag and add to list of matches
            foundIt = True
            matches.append(info)
        count += 1
    if foundIt == False:
        # No matches; return message and flag
        return notFound, False
    else:
        # Return matches and flag
        return matches, True
