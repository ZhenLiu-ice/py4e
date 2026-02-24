x, y = 6, 2
print(x >= 2 and (x / y) > 2)

x, y = 1, 0
print(x >= 2 and (x / y) > 2)

x, y = 6, 0
# print(x >= 2 and (x / y) > 2)
print(x >= 2 and y != 0 and (x / y) > 2)
