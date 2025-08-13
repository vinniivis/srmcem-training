def rotate_list(lst, k):
    if not lst:
        return []
    k = k % len(lst)
    return lst[-k:] + lst[:-k]
data = [1, 2, 3, 4, 5]
print(rotate_list(data, 2))
