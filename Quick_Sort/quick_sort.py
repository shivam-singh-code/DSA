def swap(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp


def piviot(my_list, piviot_index, end_index):
    swap_index = piviot_index
    for i in range(piviot_index + 1, end_index + 1):
        if my_list[i] < my_list[piviot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    swap(my_list, piviot_index, swap_index)
    return swap_index


def quick_sort_helper(my_list, left, right):
    if left < right:
        piviot_index = piviot(my_list, left, right)
        quick_sort_helper(my_list, left, piviot_index-1)
        quick_sort_helper(my_list, piviot_index+1, right)
    return my_list


def quick_sort(my_list):
    return quick_sort_helper(my_list, 0, len(my_list)-1)


my_list = [4,6,1,7,3,2,5]
print(quick_sort(my_list))


# Time Complexity = O(n log n) best and average
# wrost case = when list is sorted o(n^2)



