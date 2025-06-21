def three_sum(nums):
    nums.sort()
    n = len(nums)
    result = []

    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # Skip duplicate elements

        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append((i, left, right))
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1  # Skip duplicates
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1  # Skip duplicates
            elif total < 0:
                left += 1
            else:
                right -= 1

    return len(result) > 0, result


# Example usage:
nums1 = [0, 1, -1, 2]
nums2 = [1, 3, 5, 7]
print(three_sum(nums1))  # Output: (True, [(0, 1, 2)])
print(three_sum(nums2))  # Output: (False, [])
