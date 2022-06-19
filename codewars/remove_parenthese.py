# a = "example(unwanted thing)example"
# foo = list(a)
# start = foo.index("(")
# stop = foo.index(")")
# d = foo[start:stop + 1]
# print("".join(d))
# s = a.replace("".join(d), "")
# print(s)


# def remove_parentheses(s):
#     new_str = list(s)
#     start = new_str.index("(")
#     stop = new_str.index(")")
#     delete_str = new_str[start:stop + 1]
#     return s.replace("".join(delete_str), "")
#
#
# print(remove_parentheses("(first group) toto aime le) pain"))
soso = "hello example (words(more words) here) something"
t = list(soso)
# start = t.index("(")
# stop = t.index(")", -1)
z = "".join([x for x in list(soso) if x != "(" and x != ")"])
print(z)
