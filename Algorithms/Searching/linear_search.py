def linear_search(inputList, element):
    for index in range(len(inputList)):
        if inputList[index] == element:
            return index
    return -1
