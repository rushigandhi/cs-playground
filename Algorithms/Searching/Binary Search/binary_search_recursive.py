
# O(log(n)) worst case time complexity
# O(1) space complexity


def binary_search_recursive(input_list, low, high, element):

    # this means the element could not be found
    if low > high:
        return -1

    # find the middle index, guarding against overflow
    mid = low + (high - low)//2

    # if the element at mid is what we're looking for, return the middle index
    if input_list[mid] == element:
        return mid

    # else if it is greater, recursively call with the upper bound one less than the middle index
    elif input_list[mid] > element:
        return binary_search_recursive(input_list, low, mid - 1, element)

    # else (where input_list[mid] < element), recursively call with the lower bound one greater than the middle index
    else:
        return binary_search_recursive(input_list, mid + 1, high, element)
