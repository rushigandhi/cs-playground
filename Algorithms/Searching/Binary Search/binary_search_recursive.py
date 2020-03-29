def binary_search_recursive(inputList, low, high, element):
    if low > high:
        return -1
    mid = low + (high - low)//2
    if inputList[mid] == element:
        return mid
    elif inputList[mid] > element:
        return binary_search_recursive(inputList, low, mid - 1, element)
    else:
        return binary_search_recursive(inputList, mid + 1, high, element)
