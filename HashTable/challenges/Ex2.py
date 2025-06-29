def find_duplicate(list):
    num_counts = {}
    for num in list:
        num_counts[num] = num_counts.get(num, 0) + 1
    duplicates = [num for num, count in num_counts.items() if count > 1]
    return duplicates

dp_list = [4, 3, 2, 7, 8, 2, 3, 1]
print ( find_duplicate([1, 2, 3, 4, 5]) )
print ( find_duplicate([1, 1, 2, 2, 3]) )
print ( find_duplicate([1, 1, 1, 1, 1]) )
print ( find_duplicate([1, 2, 3, 3, 3, 4, 4, 5]) )
print ( find_duplicate([1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicate([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicate([]) )