
# O(log(n)) worst case time complexity
# O(1) space complexity


def binary_search_iterative(input_list, low, high, element):

    # while the lower bound is less than or equal to the upper bound
    while low <= high:

        # find the middle index, guarding against overflow
        mid = low + (high - low)//2

        # if the element at mid is what we're looking for, return the middle index
        if input_list[mid] == element:
            return mid
        # else if it is greater, make the upper bound one less than the middle index
        elif input_list[mid] > element:
            high = mid - 1
        # else (where input_list[mid] < element), make the lower bound one greater than the middle index
        else:
            low = mid + 1
    return -1
