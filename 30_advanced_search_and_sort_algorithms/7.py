def _bubble_sort(array):
    swapped = True

    #Make sure that array has at least 2 items...
    if len(array) < 2 : return "Error! Array has less than 2 items!"

    while swapped == True: #If no swaps are made, swapped = False, ending the loop
        swapped = False

        #Iterate through array...
        for i in range(0,len(array)-1):
            if array[i] > array[i+1]:
                #Store array[i] for later use...
                temp = array[i]
                
                #Swap i and i+1
                array[i] = array[i+1]
                array[i+1] = temp
                swapped = True

    return array

print(_bubble_sort([9,5,2,3,5,11,6]))

