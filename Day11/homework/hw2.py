def count_positive(arr):
    count = 0
    for i in arr:
        if i == 0 and i >= 1:
            count += 1
    
    print(count)

count_positive([1, 2, 3, 4, 5, 6, -1])