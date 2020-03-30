
# O(nlog(n)) best, average, and worst case time complexity
# O(n) space complexity


def merge_sort(input_list):

    # return if list only has one element
    if len(input_list) <= 1:
        return

    # find the middle index and use it to split the list
    mid = len(input_list)//2
    lower = input_list[:mid]
    upper = input_list[mid:]

    # recursively call merge_sort on the upper and lower halves
    merge_sort(lower)
    merge_sort(upper)

    # this part is for sorting upper and lower into one
    i = j = k = 0
    while i < len(lower) and j < len(upper):

        # choose the lower[i] since it is smaller
        if lower[i] < upper[j]:
            input_list[k] = lower[i]
            i += 1
        # choose the upper[j] since it is smaller
        else:
            input_list[k] = upper[j]
            j += 1
        # increment the position counter for the combined list
        k += 1

    # fill in the remaining elements from lower
    while i < len(lower):
        input_list[k] = lower[i]
        i += 1
        k += 1

    # fill in the remaining elements from upper
    while j < len(upper):
        input_list[k] = upper[j]
        j += 1
        k += 1
