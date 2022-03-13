import datetime
from datetime import *
from time import sleep

a = "19:07:51"
start = datetime.strptime('18:59:59', "%H:%M:%S")
end = datetime.strptime('19:05:00', "%H:%M:%S")
today = datetime.today().strftime("%H:%M:%S")
# timestamp = datetime.today().strftime('%Y-%m-%d %-H:%M:%S')
# hours = ":".join(timestamp.split(" ")[1].split(":")[0:2])

# def example():
#     print("hello")
#     sleep(1)
#
#
# while True:
#     timestamp = datetime.today().strftime('%Y-%m-%d %-H:%M:%S')
#     hours = ":".join(timestamp.split(" ")[1].split(":")[0:2])
#     if start == hours:
#         example()
#         continue
#     if hours == end:
#         break
#     sleep(1)


# while True:
#
#     sleep(1)
a = [1,2,3,4,5]
foo = [x for x in a if x % 2 == 0]
print(foo)