list_1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# list_1.insert(1, '"')
# list_1.insert(3, '"')
# list_1.insert(5, '"')
# list_1.insert(7, '"')
# list_1.insert(12, '"')
# list_1.insert(14, '"')
# union = " "
# sentence = union.join(list_1)
sentence = []
for i in list_1:
    if i.replace("+", "").replace("-", "").isdigit():
        if i.isdigit():
            sentence.append(f"'{int(i):02}'")
        else:
            sentence.append(f"'{i[0]}{int(i[1:]):02}'")
    else:
        sentence.append(i)

print(" ".join(sentence))