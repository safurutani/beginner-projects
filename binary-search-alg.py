def binary_search(list, element):
    #variables for list currently being searched through
    middle = 0
    start = 0
    end = len(list)
    steps = 1
    while (start <= end):
        #organize list in ascending order for binary search to work
        list.sort()
        print("Step", steps, ":" , str(list[start:end+1]))
        steps += 1
        middle = (start + end) // 2

        #the element has been found
        if element == list[middle]:
            return middle
        #discards the 2nd half of the list so it can search the 1st part next
        if element < list[middle]:
            end = middle - 1
        #discards the 1st half of the list so it can search the 2nd part next
        else:
            start = middle + 1
    return -1
numbers = [2, 4, 100, 31, 5, 8, 12, 22, 56, 90]
target = 100

binary_search(numbers, target)