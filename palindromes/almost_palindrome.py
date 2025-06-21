def is_palindrome(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


def almost_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            # Try removing either the left or the right character
            return is_palindrome(s, left + 1, right) or is_palindrome(
                s, left, right - 1
            )
        left += 1
        right -= 1
    return True


# Example usage
print(almost_palindrome("tacocats"))  # Output: True
print(almost_palindrome("racercar"))  # Output: True
print(almost_palindrome("kbayak"))  # Output: True
print(almost_palindrome("acbccba"))  # Output: True
print(almost_palindrome("abccbca"))  # Output: True
print(almost_palindrome("madam"))  # Output: True
