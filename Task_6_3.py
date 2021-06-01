from json import dump
from itertools import zip_longest

with open("users.csv", "r", encoding="utf-8") as users:
    with open("hobby.csv", "r", encoding="utf-8") as hobby:
        if len(users.readline()) > len(hobby.readline()):
            with open("full_dict.json", "w", encoding="utf-8") as f:
                full_list = zip_longest((" ".join(us.split(",")) for us in users), hobby, fillvalue=None)
                dict = {str(el[0]).strip(): (el[1].strip()) for el in full_list}
                dump(dict, f, ensure_ascii=False, indent=4)
            print(dict)
        else:
            exit(1)