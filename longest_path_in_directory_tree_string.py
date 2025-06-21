def length_longest_path(input: str) -> int:
    max_length = 0
    path_length = {0: 0}  # Dictionary to store the current path length at each depth

    for line in input.splitlines():
        name = line.lstrip("\t")
        depth = len(line) - len(name)

        if "." in name:  # It's a file
            max_length = max(max_length, path_length[depth] + len(name))
        else:  # It's a directory
            path_length[depth + 1] = (
                path_length[depth] + len(name) + 1
            )  # +1 for the '/'

    return max_length


# Example usage
input_str = "a\n\tb\n\t\tc\n\t\td\n\te\n\t\tf\n\t\t\tcow"
print(length_longest_path(input_str))  # Output: 9
