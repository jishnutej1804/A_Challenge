# Problem: Valid Palindrome - A string is a palindrome if it reads the same forward and backward.
# Approach: Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)

def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:

        # Skip non-alphanumeric characters
        while left < right and not s[left].isalnum():
            left += 1

        while left < right and not s[right].isalnum():
            right -= 1

        # Compare characters ignoring case
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


# Test Cases
# Test Cases
print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("race a car"))                       # False
print(is_palindrome(" "))                                # True
print(is_palindrome("Madam"))                            # True
print(is_palindrome(".,!"))                              # True
print(is_palindrome("0P"))                               # False