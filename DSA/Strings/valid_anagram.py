# Problem: Valid Anagram - Two strings are anagrams if they contain exactly the same letters with the same frequency, but possibly in a different order
# Approach: Frequency Map
# Time Complexity: O(n)
# Space Complexity: O(1)

def is_anagram(s, t):
    if len(s) != len(t):
        return False

    count = [0] * 26

    for i in range(len(s)):
        count[ord(s[i]) - ord('a')] += 1
        count[ord(t[i]) - ord('a')] -= 1

    return all(x == 0 for x in count)


# Test Cases
print(is_anagram("anagram", "nagaram"))  # True
print(is_anagram("rat", "car"))          # False
print(is_anagram("a", "a"))              # True