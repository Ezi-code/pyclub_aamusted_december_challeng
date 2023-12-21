# Ezi-code

def find_missing_number(arr):
    n = len(arr) + 1
    expected_sum = (n * (n + 1)) // 2
    actual_sum = sum(arr)
    missing_number = expected_sum - actual_sum
    return missing_number

# Example usage
arr = [1, 2, 4, 5, 6]
missing_number = find_missing_number(arr)
print(f"The missing number is: {missing_number}")
