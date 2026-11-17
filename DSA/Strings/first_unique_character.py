
def first_uniq_char(s):
    frequency = {}

    # Count the frequency of each character
    for char in s:
        frequency[char] = frequency.get(char, 0) + 1

    # Find the first character that appears only once
    for i, char in enumerate(s):
        if frequency[char] == 1:
            return i

    return -1


print(first_uniq_char("leetcode"))
print(first_uniq_char("loveleetcode"))
print(first_uniq_char("aabb"))
print(first_uniq_char("a"))
print(first_uniq_char(""))

