def can_partition(arr):
    total_sum = sum(arr)

    # If the total sum is odd, it cannot be split into two equal parts
    if total_sum % 2 != 0:
        return False

    target_sum = total_sum // 2
    current_sum = 0

    for i in range(len(arr)):
        current_sum += arr[i]

        if current_sum == target_sum:
            return True, (arr[: i + 1], arr[i + 1 :])

    return False


# Test cases
print(can_partition([5, 2, 3]))  # Output: (True, ([5], [2, 3]))
print(
    can_partition([2, 3, 2, 1, 1, 1, 2, 1, 1])
)  # Output: (True, ([2, 3, 2], [1, 1, 1, 2, 1, 1]))
print(can_partition([1, 1, 3]))  # Output: False
print(can_partition([1, 1, 3, 1]))  # Output: False
