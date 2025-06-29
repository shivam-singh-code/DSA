# Time complexity of O(n^2)
def item_in_common(list1, list2):
    for i in list1:
        for j in list2:
            if i==j:
                return True
    return False

list1 = [1,3,5]
list2 = [2,4,5]

print(item_in_common(list1, list2))

# Time Complexity of O(n)
def item_in_common_optimized(list1, list2):
    list_dict = {}
    for i in list1:
        list_dict[i] = True
    for j in list2:
        if j in list_dict:
            return True
    return False

list1 = [1,3,5]
list2 = [2,4,6]

print(item_in_common(list1, list2))