def atoi(s):
    """
    Converts an array of ASCII characters to an integer.

    Args:
        s (str): The input string.

    Returns:
        int: The integer represented by the input string.

    Raises:
        ValueError: If the input string is not a valid integer representation.
    """

    # Remove leading whitespace
    s = s.lstrip()

    # Check for negative sign
    sign = 1
    if s and s[0] == "-":
        sign = -1
        s = s[1:]
    elif s and s[0] == "+":
        s = s[1:]

    # Initialize result
    result = 0

    # Iterate over characters
    for c in s:
        if c.isdigit():
            # Update result
            result = result * 10 + ord(c) - ord("0")
        else:
            # Stop parsing on non-digit characters
            break

    # Apply sign
    result *= sign

    # Clamp to 32-bit signed integer range
    result = max(-(2**31), min(result, 2**31 - 1))

    return result


# Example usage:
print(atoi("42"))  # Output: 42
print(atoi("   -42"))  # Output: -42
print(atoi("4193 with words"))  # Output: 4193
