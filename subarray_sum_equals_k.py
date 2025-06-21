def subarraySum(nums, k) -> int:
    count = 0
    cumulative_sum = 0
    sum_map = {0: 1}  # Initialize with 0 sum having one occurrence

    for num in nums:
        cumulative_sum += num
        if (cumulative_sum - k) in sum_map:
            count += sum_map[cumulative_sum - k]
        sum_map[cumulative_sum] = sum_map.get(cumulative_sum, 0) + 1

    return count


# Test cases
assert subarraySum([1, 1, 1], 2) == 2
assert subarraySum([1, 2, 3], 3) == 2
