from itertools import islice, zip_longest

tutors_names = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses_numbers = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

# zipped_values = zip(tutors_names, klasses_numbers)
# zipped_list = list(zipped_values)

# print(zipped_list)
# print(type(zipped_list))

result = (i for i in zip_longest(tutors_names, klasses_numbers))
print(type(result))
print(*islice(result, 10))