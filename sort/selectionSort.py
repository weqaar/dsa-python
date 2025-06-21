# Selection Sort

# Ascending sort - variant 1
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Ascending sort - variant 2
def sort_ascending(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                tmp = arr[j]
                arr[j] = arr[i]
                arr[i] = tmp
    return arr

# Descending sort
def sort_descending(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] < arr[j]:
                tmp = arr[i]
                arr[i] = arr[j]
                arr[j] = tmp
    return arr



if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Sorted - ascending (variant 1):", selection_sort(arr))
    print("Sorted - ascending (variant 2):", sort_ascending(arr))
    print("Sorted - descending:", sort_descending(arr))