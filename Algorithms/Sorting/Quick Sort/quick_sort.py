
# O(nlog(n)) best and average case, while the worst case has O(n^2) time complexity
# O(log(n)) space complexity due to stack frames (from recursive calls)

# This quicksort implementation is done with the pivot
# being the median of the first, last and middle element
# in the input list

# create_partition helps partition the list into < pivot and > pivot, and returns the borderIndex


def create_partition(inputList, start, end):

    # get pivot and set it as the first element in the list
    pivotIndex = get_pivot(inputList, start, end)
    pivotValue = inputList[pivotIndex]
    inputList[pivotIndex], inputList[start] = inputList[start], inputList[pivotIndex]

    # at the end the border is going to be where the pivot resides
    borderIndex = start

    # from start to end inclusive
    for i in range(start, end + 1):

        # if the current value is less than the pivot value
        if inputList[i] < pivotValue:

            # increment the borderIndex
            borderIndex += 1
            # swap the border value with the current value
            inputList[i], inputList[borderIndex] = inputList[borderIndex], inputList[i]

    # swap the border value with the pivotValue
    inputList[start], inputList[borderIndex] = inputList[borderIndex], inputList[start]

    return borderIndex


# get_pivot returns the median of the start, middle and end values as the pivot
def get_pivot(inputList, start, end):

    # find the middle index, guarding against overflow
    mid = start + (end - start)//2
    pivot = end

    # find the median of start, mid, and end
    if inputList[start] < inputList[mid]:
        if inputList[mid] < inputList[end]:
            pivot = mid
    elif inputList[start] < inputList[end]:
        pivot = start
    return pivot


def quick_sort_recursive(inputList, start, end):

    if start < end:
        # get the splitting borderIndex, and recursively call on the upper and lower halves
        borderIndex = create_partition(inputList, start, end)
        quick_sort_recursive(inputList, start, borderIndex - 1)
        quick_sort_recursive(inputList, borderIndex + 1, end)


def quick_sort(inputList):
    quick_sort_recursive(inputList, 0, len(inputList) - 1)
