def rotate_array(arr, k):
    n = len(arr)
    k = k % n  # handle cases where k is larger than the array length
    return arr[-k:] + arr[:-k]
