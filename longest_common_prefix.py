from typing import List


def lcp(str_arr: List[str]) -> str:
    if not str_arr:
        return ""

    # Start with the first string as the initial prefix
    prefix = str_arr[0]

    # Compare the prefix with each string in the array
    for string in str_arr[1:]:
        # Update the prefix to the common prefix with the current string
        while not string.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""

    return prefix


# Example usage
arr = ["catsup", "cats", "catamaran"]
print(lcp(arr))  # Output: "cat"
