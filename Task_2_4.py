list_1 = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
name = [list_1[0][-5:], list_1[1][-6:], list_1[2][-7:], list_1[3][-6:]]
for n in name:
    greeting = "Привет, " + n  + "!"
    print(greeting.title())