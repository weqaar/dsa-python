def sumSubarrayMins(nums) -> int:
    MOD = 10**9 + 7
    n = len(nums)

    # Arrays to store the previous and next smaller elements
    prev_smaller = [-1] * n
    next_smaller = [n] * n

    # Monotonic stack for previous smaller elements
    stack = []
    for i in range(n):
        while stack and nums[stack[-1]] > nums[i]:
            stack.pop()
        prev_smaller[i] = stack[-1] if stack else -1
        stack.append(i)

    # Monotonic stack for next smaller elements
    stack = []
    for i in range(n):
        while stack and nums[stack[-1]] > nums[i]:
            next_smaller[stack.pop()] = i
        stack.append(i)

    # Calculate the sum of minimums
    result = 0
    for i in range(n):
        left_count = i - prev_smaller[i]
        right_count = next_smaller[i] - i
        result += nums[i] * left_count * right_count
        result %= MOD

    return result


# Test cases
assert sumSubarrayMins([3, 1, 2, 4]) == 17
assert sumSubarrayMins([11, 81, 94, 43, 3]) == 444
