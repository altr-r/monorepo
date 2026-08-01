def bubble_sort(collection):
    n = len(collection)

    for i in range(n):
        for j in range(n - 1 - i):
            if collection[j + 1] < collection[j]:
                collection[j + 1], collection[j] = collection[j], collection[j +1]
    return collection