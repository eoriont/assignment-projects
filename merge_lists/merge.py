def merge(arr1, arr2):
    result = []
    i, j = 0, 0
    while len(arr1) > i and len(arr2) > j:
        e1 = arr1[i]
        e2 = arr2[j]
        if e1 < e2:
            result.append(e1)
            i += 1
        else:
            result.append(e2)
            j += 1
    result += arr1[i:]
    result += arr2[j:]
    return result


a1 = [1, 3, 5, 7, 9, 11]
a2 = [2, 4, 6, 8, 10, 12]

print(merge(a1, a2))
