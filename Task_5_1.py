def numbers_range(n):
    for i in range(n+1):
        yield i
a = numbers_range(11)
print(type(a))
for b in a:
    if b % 2 != 0:
        print(b)
