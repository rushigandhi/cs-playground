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
