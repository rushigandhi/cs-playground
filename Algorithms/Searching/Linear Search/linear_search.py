
# O(n) worst case time complexity
# O(1) space complexity


def linear_search(inputList, element):

    # iterate through the list until you find the element you're looking for
    for index in range(len(inputList)):
        if inputList[index] == element:
            return index
    return -1
