def is_palindrome(x):
    return str(x) == str(x)[::-1]


def is_prime(x):
    if x < 2:
        return False
    if x in (2, 3):
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    i = 5
    while i * i <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return False
        i += 6
    return True


def primePalindrome(n):
    if 8 <= n <= 11:
        return 11  # Special case, as 11 is the only two-digit prime palindrome
    x = n
    while True:
        if is_palindrome(x) and is_prime(x):
            return x
        x += 1
        # Skip even numbers and multiples of 10 to optimize
        if 10**7 < x < 10**8:
            x = 10**8


# Test cases
assert primePalindrome(6) == 7
assert primePalindrome(8) == 11
assert primePalindrome(13) == 101
