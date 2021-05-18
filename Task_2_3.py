list_1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for i, v in enumerate(list_1):
    if v.replace("+", "").replace("-", "").isdigit():
        if v.isdigit():
            list_1[i] = (f"'{int(v):02}'")
        else:
            list_1[i] = f"'{v[0]}{int(v[1:]):02}'"

print(" ".join(list_1))