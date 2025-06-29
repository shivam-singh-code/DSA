def group_anagram(strings):
    anagram_group = {}
    for string in strings:
        canonical = ''.join(sorted(string))
        if canonical in anagram_group:
            anagram_group[canonical].append(string)
        else:
            anagram_group[canonical] = [string]
    # print(anagram_group)
    return list(anagram_group.values())
    
print("1st set:")
print( group_anagram(["eat", "tea", "tan", "ate", "nat", "bat"]) )

print("\n2nd set:")
print( group_anagram(["abc", "cba", "bac", "foo", "bar"]) )

print("\n3rd set:")
print( group_anagram(["listen", "silent", "triangle", "integral", "garden", "ranged"]) )