#Recursive variant of the binary search...

def _binary_search(array,search_term,bottom,top):
    #Assign middle of bottom and top...
    middle = (top + bottom) // 2

    #DEBUG PRINT
    print(array[middle])

    #Seach term found...
    if array[middle] == search_term:
        return ("Search term found!")
    else: #Search term not found...
        if array[middle] < search_term:
            bottom = middle + 1
        else:
            top = middle - 1

    #If term not found, call definition again...
    return(_binary_search(array,search_term,bottom,top))


#START
array = [1, 3, 5, 7, 9, 11, 13]
print(_binary_search(array,7,0,len(array)))