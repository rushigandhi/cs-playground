def bubble_sort(inputList):
    # due to a nested iteration through the whole input list, the worst case time complexity is O(n^2)
    for i in range(len(inputList)):
        for j in range(len(inputList) - 1 - i):
            if(inputList[j] > inputList[j + 1]):
                temp = inputList[j]
                inputList[j] = inputList[j + 1]
                inputList[j + 1] = temp
