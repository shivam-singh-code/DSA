def first_non_repeating_char(string):
    char_count = {}
    for c in string:
        char_count[c] = char_count.get(c, 0) + 1
    
    for c in string:
        if char_count[c] == 1:
            return c
    return None

print(first_non_repeating_char('leetcode'))
print(first_non_repeating_char('hello'))
print(first_non_repeating_char('hh'))