def checkSubarraySum(nums, k) -> bool:
    # Dictionary to store the remainder and its index
    remainder_map = {0: -1}
    cumulative_sum = 0

    for i, num in enumerate(nums):
        cumulative_sum += num
        remainder = cumulative_sum % k if k != 0 else cumulative_sum

        if remainder in remainder_map:
            if i - remainder_map[remainder] > 1:
                return True
        else:
            remainder_map[remainder] = i

    return False


# Test cases
assert checkSubarraySum([23, 2, 4, 6, 7], 6) == True
assert checkSubarraySum([23, 2, 6, 4, 7], 6) == True
assert checkSubarraySum([23, 2, 6, 4, 7], 13) == False
