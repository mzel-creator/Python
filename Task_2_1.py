#1
a = 15 * 3
b = 15 / 3
c = 15 // 2
d = 15 ** 2
print(type(a))
print(type(b))
print(type(c))
print(type(d))

#2
print(isinstance(a, int))
print(isinstance(b, float))
print(isinstance(c, int))
print(isinstance(d, int))

#3
result = [a, b, c, d]
for i in result:
    print(type(i ))
