from collections import Counter


def can_form_palindrome(s):
    char_count = Counter(s)
    odd_count = sum(1 for count in char_count.values() if count % 2 != 0)
    return odd_count <= 1


# Example usage
print(can_form_palindrome("facebface"))  # Output: True
print(can_form_palindrome("facebookface"))  # Output: False
