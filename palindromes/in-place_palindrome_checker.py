import re


def is_palindrome(s: str) -> bool:
    # Remove non-alphanumeric characters and convert to lowercase
    normalized_str = re.sub(r"[^a-zA-Z0-9]", "", s).lower()
    # Check if the string is equal to its reverse
    return normalized_str == normalized_str[::-1]


# Example usage
print(is_palindrome("Race car"))  # Output: True
print(is_palindrome("A man, a plan, a canal -- Panama!"))  # Output: True
print(is_palindrome("No lemon, no melon."))  # Output: True
