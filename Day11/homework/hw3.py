def averge_list(arr):
    count = 0
    for i in arr:
        count += 1
        print(i * count // count)

averge_list([1, 2, 3, 4, 5])