import json
BODY_PRIMARY = {"deviceid": "", "data": {}}

status = "on"
BODY_PRIMARY["data"] = dict({"switch": status})

print(BODY_PRIMARY)

a = [12,23,47]

foo = [x for x in a if x %2 == 1]
print(foo)


