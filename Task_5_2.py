lower = int(input("Введите нижнюю границу диапазона: "))
upper = int(input("Введите верхнюю границу диапазона: "))
for i in range(lower, upper+1):
    if(i % 2 != 0):
        print(i)

#_________________________________________________________

print(*[num for num in range(lower, upper + 1, 2)])