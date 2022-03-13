def equal_array(arr1, arr2):
    result = False
    for i in arr1:
        if i in arr2:
            result = True
        else:
            result = False
    return result


def next_smaller(n):
    for i in range(n, 0, -1):
        if len([int(x) for x in str(n)]) == len([int(x) for x in str(i)]):
            print(i)


next_smaller(100)
