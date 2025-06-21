def depth_sum(nested_list):
    def dfs(nested_list, depth):
        total = 0
        for item in nested_list:
            if isinstance(item, int):
                total += item * depth
            else:
                total += dfs(item, depth + 1)
        return total

    return dfs(nested_list, 1)


# Example usage:
print(depth_sum([4, [5, 6]]))  # Output: 26
print(depth_sum([8, 4, [5, [9], 3], 6]))  # Output: 61
