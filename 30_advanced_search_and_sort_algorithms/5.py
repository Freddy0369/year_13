def _binary_search(array,search_term):
    found = False
    top = len(array)
    bottom = 0
    middle = 0

    #Loop through array, splitting in half until value is found...
    while found == False and top != bottom:
        middle = (top + bottom) // 2
        print(array[middle])

        #Seach term found
        if array[middle] == search_term:
            return ("Search term found!")
        else: #Search term not found
            if array[middle] < search_term:
                bottom = middle + 1
            else:
                top = middle - 1

    #Not found, array fully iterated...
    return ("Error! Search term "+str(search_term)+" not found!")

array = [10,20,30,40,50]
print(_binary_search(array,35))