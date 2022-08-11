def modify_multiply(st, loc, num):
    foo = (st.split()[loc] + "-") * num
    return foo[:-1]


# modify_multiply("This is a string", 3, 5)


# solution code ware
def modify_multiply(st, loc, num):
    return '-'.join([st.split()[loc]] * num)


def solution(n):
    return 7


print(solution(4))
