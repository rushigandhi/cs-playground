
# O(nlog(n)) best and average case, while the worst case has O(n^2) time complexity
# O(log(n)) space complexity due to stack frames (from recursive calls)

# This quicksort implementation is done with the pivot
# being the median of the first, last and middle element
# in the input list

# create_partition helps partition the list into < pivot and > pivot, and returns the borderIndex


def create_partition(input_list, start, end):

    # get pivot and set it as the first element in the list
    pivotIndex = get_pivot(input_list, start, end)
    pivotValue = input_list[pivotIndex]
    input_list[pivotIndex], input_list[start] = input_list[start], input_list[pivotIndex]

    # at the end the border is going to be where the pivot resides
    borderIndex = start

    # from start to end inclusive
    for i in range(start, end + 1):

        # if the current value is less than the pivot value
        if input_list[i] < pivotValue:

            # increment the borderIndex
            borderIndex += 1
            # swap the border value with the current value
            input_list[i], input_list[borderIndex] = input_list[borderIndex], input_list[i]

    # swap the border value with the pivotValue
    input_list[start], input_list[borderIndex] = input_list[borderIndex], input_list[start]

    return borderIndex


# get_pivot returns the median of the start, middle and end values as the pivot
def get_pivot(input_list, start, end):

    # find the middle index, guarding against overflow
    mid = start + (end - start)//2
    pivot = end

    # find the median of start, mid, and end
    if input_list[start] < input_list[mid]:
        if input_list[mid] < input_list[end]:
            pivot = mid
    elif input_list[start] < input_list[end]:
        pivot = start
    return pivot


def quick_sort_recursive(input_list, start, end):

    if start < end:
        # get the splitting borderIndex, and recursively call on the upper and lower halves
        borderIndex = create_partition(input_list, start, end)
        quick_sort_recursive(input_list, start, borderIndex - 1)
        quick_sort_recursive(input_list, borderIndex + 1, end)


def quick_sort(input_list):
    quick_sort_recursive(input_list, 0, len(input_list) - 1)
