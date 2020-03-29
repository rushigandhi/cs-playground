
# O(nlog(n)) best, average, and worst case time complexity
# O(n) space complexity


def merge_sort(inputList):

    # return if list only has one element
    if len(inputList) <= 1:
        return

    # find the middle index and use it to split the list
    mid = len(inputList)//2
    lower = inputList[:mid]
    upper = inputList[mid:]

    # recursively call merge_sort on the upper and lower halves
    merge_sort(lower)
    merge_sort(upper)

    # this part is for sorting upper and lower into one
    i = j = k = 0
    while i < len(lower) and j < len(upper):

        # choose the lower[i] since it is smaller
        if lower[i] < upper[j]:
            inputList[k] = lower[i]
            i += 1
        # choose the upper[j] since it is smaller
        else:
            inputList[k] = upper[j]
            j += 1
        # increment the position counter for the combined list
        k += 1

    # fill in the remaining elements from lower
    while i < len(lower):
        inputList[k] = lower[i]
        i += 1
        k += 1

    # fill in the remaining elements from upper
    while j < len(upper):
        inputList[k] = upper[j]
        j += 1
        k += 1
