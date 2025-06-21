"""
Given two strings text1 and text2, return the length of their longest mutual substring. If there is no mutual substring, return 0.


A substring of a string is a contiguous portion of that string. Strings can be substrings of themselves.  E.g.  substrings of “topace” include “top”, “ace”, “pace”, and “topace” itself.


A mutual substring of two strings is a substring that occurs in both strings.


Example 1:
Input: text1 = "abcdef", text2 = "def"
Output: 3
Explanation: “def” is of length 3 and is a valid substring in both text1 and text2.

Example 2:
Input: text1 = "textualinput", text2 = "yz123"
Output: 0
Explanation: there are no mutual substrings between these two strings

Example 3:
Input: text1 = "abcde", text2 = "bc"
Output: 2
Explanation: “bc” is a contiguous substring of both text1, text2

Example 4:
Input: text1 = "cx", text2 = "abc"
Output: 1
Explanation: “c” is a contiguous substring of both text1, text2

"""


# Solution 1: Sliding Window Approach
def longest_common_substring(text1, text2):
    longer, shorter = (text1, text2) if len(text1) >= len(text2) else (text2, text1)

    frame_sz = len(shorter)
    while frame_sz > 0:
        for start in range(len(shorter) - frame_sz + 1):
            chunk = shorter[start : start + frame_sz]
            if chunk in longer:
                return len(chunk)
        frame_sz -= 1
    return 0


# Solution 2: Precompute Substrings
def greatest_common_substring(text1, text2):
    if text1 == text2:
        return len(text1)

    if len(text1) >= len(text2):
        long_string = text1
        short_string = text2
    else:
        long_string = text2
        short_string = text1

    substrings = [
        short_string[i : i + j]
        for j in range(len(short_string), 0, -1)
        for i in range(len(short_string) - j + 1)
    ]

    for s in substrings:
        if s in long_string:
            return len(s)
    return 0
