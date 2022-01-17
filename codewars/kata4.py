def array_digit_number(number):
    return [int(x) for x in str(number)]


def next_smaller(n):
    result = []
    foo = array_digit_number(n)
    while n > 0:
        n = n - 1
        for i in array_digit_number(n):
            if i in foo:
                result.append(i)

    return result


print(next_smaller(21))
