# print("Hello, World!")
# print("How's it going?")
#
# a = "I'm"
# b = '"batman"'
# c = 5
# d = 6
#
# print(a, b)
# print(a + " " + b)
# print(a, b, c, sep="\n")
# print(c == d)
#
# e = bool(c == d)
# # print(float(e))
#
# f = not (c == d)
# # print(f)
#
# g = c is d
# print(g)
# print(d/c)
# print(-15%7) # add the divisor if dividend is negative
#
# st = "8"
# num = 8
#
# # print(int(st) + num)
# # st = "mute"
# print(st)
#
# if int(st) is num:
#     print("Not equal")
# else: print("Equal")
#
# multiLine = """Si vis Pacem,
# ParaBellum."""
# ft = 2.3
# inte = 1
# print(ft + inte)
# print(multiLine)
#
# helo = "I'm the Batman"
#
# # print(helo[:4] + helo[8:])
#
# print(helo[-1])
# print(helo[-10: -3].upper())
# print(len(helo))
#
# an = 1
# bo = "hello"
#
# print(f"{bo} {an} {an + 2}")
#
# n = 5
#
#
# for x in range(1, n+1):
#     print(x, end="")

# def swap_case(s):
#     for x in range(s):
#         if x.isupper():
#             x.lower()
#         elif x.islower():
#             x.upper()
#         else: continue
#     return s
#
# if __name__ == '__main__':
#     print("Enter a string: ")
#     s = input()
#     result = swap_case(s)
#     print(result)

a = [1, 2, 3]

# b = a
# b.copy(a)
b = a.copy()

b[1] = 11

print(a)
print(b)