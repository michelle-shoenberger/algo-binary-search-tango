# Binary search
# Sort the input
# Iniitalize two pointers for the range of the search
# Half the range - if > or < middle value

def binary_search(target, arr):
    arr.sort()
    indices = [0, len(arr)-1]
    while indices[1] - indices[0] > 0:
        middle_idx = ((indices[1] - indices[0]) // 2) + indices[0]
        middle = arr[middle_idx]
        if middle == target:
            return middle_idx
        elif target < middle:
            indices[1] = middle_idx - 1
        else:
            indices[0] = middle_idx + 1
    if arr[indices[0]] == target: return indices[0]
    return -1