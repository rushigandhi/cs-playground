
# O(n^2) worst case time complexity
# O(1) space complexity


def bubble_sort(input_list):

    # nested for loops for traversal
    for i in range(len(input_list)):
        for j in range(len(input_list) - 1 - i):

            # swap neighbouring elements if the previous is greater than the next
            if(input_list[j] > input_list[j + 1]):
                temp = input_list[j]
                input_list[j] = input_list[j + 1]
                input_list[j + 1] = temp
