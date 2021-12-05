# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 55]
# name = ["stephane"]


# def filter_by_mutlipe(array_number, multiple):
#     try:
#         resultat = [num for num in array_number if num % multiple == 0]
#         return resultat if resultat else "no results"
#     except:
#         return "wrong value error"


# nums_Once_Two = [x * 2 for x in nums]
# array_multiple_of_two = [x for x in nums if x % 2 == 0]

# print(filter_by_mutlipe(nums, 100))

# list1 = [10, 15, 20, 25, 30, 35, 40]
# list2 = [25, 40, 35]
# set_difference = set(list1) - set(list2)
# list_difference = list(set_difference)
# # print(list_difference)


# # print(set(list1) - set(list2))
# my_set = {1, 2, 3, 1}
# # print(my_set)

# arr = [1, 2, 3, 0, 9, 5, 0, 0, 10, 8, 0, 5, 0]

# for num in arr:
#     if num == 0:
#         arr.remove(num)


# a = 168
# b = 18


# def arrNumber(number):
#     return [int(x) for x in str(number)]


# def add(num1, num2):
#     arr_num1 = arrNumber(num1)
#     arr_num2 = arrNumber(num2)
#     return


# print(add(168, 18))


def special_number(number):
    special_numbers = [0, 1, 2, 3, 4, 5]
    array_numbers = [int(x) for x in str(number)]
    count = 0
    for num in array_numbers:
        if num in special_numbers:
            count += 1
    if count == len(str(number)):
        return "Special!!"
    else:
        return "NOT!!"


num = 444

while num > 0:
    num = round(num / 2)
    if num == 1:
        print("puissance")
        break
