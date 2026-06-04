def count_manual(arr, i):
    rep = 0
    for num in arr:
        if num == i:
            rep += 1
    print(rep)

count_manual([1, 2, 3, 4, 5, 5], 5)