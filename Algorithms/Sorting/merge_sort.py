def merge_sort(inputList):

    if len(inputList) <= 1:
        return

    mid = len(inputList)//2
    lower = inputList[:mid]
    upper = inputList[mid:]

    merge_sort(lower)
    merge_sort(upper)

    i = j = k = 0
    while i < len(lower) and j < len(upper):
        if lower[i] < upper[j]:
            inputList[k] = lower[i]
            i += 1
        else:
            inputList[k] = upper[j]
            j += 1
        k += 1

    while i < len(lower):
        inputList[k] = lower[i]
        i += 1
        k += 1

    while j < len(upper):
        inputList[k] = upper[j]
        j += 1
        k += 1
