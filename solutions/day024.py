# Ezi-code

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Example usage:
my_list = [5, 2, 4, 6, 1, 3]
insertion_sort(my_list)
print(my_list)
