data = [
    {'name': 'Joe', 'age': 20},
    {'name': 'Bill', 'age': 30},
    {'name': 'Kate', 'age': 23}
]


def itemgetter(item):
    return item['name']


def get_names(data):
    return list(map(itemgetter, data))


# print(get_names(data))


num1 = [1, 2, 3]
num2 = [5,6,7]


def adition_array(number):
    return number %2 == 0


foor = list(filter(adition_array, num1))
print(foor)
