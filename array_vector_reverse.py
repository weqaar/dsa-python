def reverse_subarray(arr, start, end):
    """
    Reverses the elements in the array `arr` between indices `start` and `end` (inclusive).
    """
    if start < 0 or end >= len(arr) or start > end:
        raise ValueError("Invalid start or end indices")

    # Reverse the subarray in place
    arr[start : end + 1] = arr[start : end + 1][::-1]


def main():
    # Example usage
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    start = 2
    end = 5
    print("Original array:", arr)
    reverse_subarray(arr, start, end)
    print("Array after reversing between indices", start, "and", end, ":", arr)


if __name__ == "__main__":
    main()
