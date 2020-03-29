def binary_search_iterative(inputList, low, high, element):
    while low <= high:
        mid = low + (high - low)//2
        if inputList[mid] == element:
            return mid
        elif inputList[mid] > element:
            high = mid - 1
        else:
            low = mid + 1
    return -1
