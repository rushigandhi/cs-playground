
# O(n) worst case time complexity
# O(1) space complexity


def linear_search(input_list, element):

    # iterate through the list until you find the element you're looking for
    for index in range(len(input_list)):
        if input_list[index] == element:
            return index
    return -1
