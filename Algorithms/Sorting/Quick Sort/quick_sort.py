# This quicksort implementation is done with the pivot
# being the median of the first, last and middle element
# in the input list


def create_partition(inputList, start, end):
    pivotIndex = get_pivot(inputList, start, end)
    pivotValue = inputList[pivotIndex]
    inputList[pivotIndex], inputList[start] = inputList[start], inputList[pivotIndex]
    borderIndex = start

    for i in range(start, end + 1):
        if inputList[i] < pivotValue:
            borderIndex += 1
            inputList[i], inputList[borderIndex] = inputList[borderIndex], inputList[i]
    inputList[start], inputList[borderIndex] = inputList[borderIndex], inputList[start]

    return borderIndex


def get_pivot(inputList, start, end):

    mid = start + (end - start)//2
    pivot = end

    if inputList[start] < inputList[mid]:
        if inputList[mid] < inputList[end]:
            pivot = mid
    elif inputList[start] < inputList[end]:
        pivot = start
    return pivot


def quick_sort_recursive(inputList, start, end):
    if start < end:
        partition = create_partition(inputList, start, end)
        quick_sort_recursive(inputList, start, partition - 1)
        quick_sort_recursive(inputList, partition + 1, end)


def quick_sort(inputList):
    quick_sort_recursive(inputList, 0, len(inputList) - 1)
