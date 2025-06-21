import re


def isPalindrome(s: str) -> bool:
    # Remove non-alphanumeric characters and convert to lowercase
    normalized_str = re.sub(r"[^a-zA-Z0-9]", "", s).lower()
    # Check if the string is equal to its reverse
    return normalized_str == normalized_str[::-1]


# Test cases
assert isPalindrome("A man, a plan, a canal: Panama") == True
assert isPalindrome("race a car") == False
assert isPalindrome(" ") == True
