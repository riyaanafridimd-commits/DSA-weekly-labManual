def merge_sort(arr):
    # Base case: a list of length 0 or 1 is already sorted
    if len(arr) <= 1:
        return arr

    # Divide: find the middle and split the array
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Conquer: merge the sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    sorted_arr = []
    i = j = 0

    # Compare elements from both lists and append the smaller one
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    # Append any remaining elements
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
