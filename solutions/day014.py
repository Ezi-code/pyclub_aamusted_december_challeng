numbers = [1, 2, 3, 4, 5,2, 6, 7, 8, 9]

for i in numbers:
    if numbers.count(i) > 1:
        print(f"dupplicate {i} found")
        continue
    