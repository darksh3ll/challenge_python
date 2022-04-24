import string


# def printer_error(s):
#   alpha = string.ascii_lowercase[0:13]
#   count = len(s)
#   error = 0
#   for i in s:
#     if i not in alpha:
#         error += 1

#   return f"{error}/{count}"

# refacto
def printer_error(s):
    alpha = string.ascii_lowercase[0:13]
    error = len([x for x in s if x not in alpha])
    return f"{error}/{len(s)}"


print(printer_error("aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"))
