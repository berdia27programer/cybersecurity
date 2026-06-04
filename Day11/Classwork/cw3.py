def filter_evens(array):
    result = []

    for i in array:
        if i % 2 == 0:
            result.append(i)
        else:
            return

filter_evens([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])