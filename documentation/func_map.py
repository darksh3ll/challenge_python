num1 = [1, 2, 10]
num2 = [10, 2, 10]

result = list(map(lambda x, y: x + y, num1, num2))  # [11, 4, 20]
multipy = list(map(lambda x: x * 2, num1))
# foo = [x * 200 for x in num1]
# is_odd = list(map(lambda x, y: x, y, num1, num2))
# print(is_odd)
gg = list(map(lambda x, y: x * y, num1, num2))
