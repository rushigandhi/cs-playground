
# O(n^2) worst case time complexity
# O(1) space complexity


def bubble_sort(inputList):

    # nested for loops for traversal
    for i in range(len(inputList)):
        for j in range(len(inputList) - 1 - i):

            # swap neighbouring elements if the previous is greater than the next
            if(inputList[j] > inputList[j + 1]):
                temp = inputList[j]
                inputList[j] = inputList[j + 1]
                inputList[j + 1] = temp
