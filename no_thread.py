numbers = []


def gen_number():
    for i in range(500000):
        numbers.append(i)
    return numbers


def is_mutiple_two():
    return [x for x in numbers if x % 2 == 0]


print(gen_number())
print("""


""")
print(is_mutiple_two())

