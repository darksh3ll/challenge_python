import threading

numbers = []


def gen_number():
    for i in range(100):
        numbers.append(i)
    return numbers


def is_mutiple_two():
    return [x for x in numbers if x % 2 == 0]


th1 = threading.Thread(target=gen_number())
th2 = threading.Thread(target=is_mutiple_two())
th1.start()
th2.start()

th1.join()
th2.join()
print("""


""")
print(is_mutiple_two())
