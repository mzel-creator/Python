import os

folder = {"my_project": [{"settings": []}, {"mainapp": []}, {"adminapp": []}, {"authapp": []}]}
for key, val in folder.items():
    if not os.path.exists(key):
        for item in val:
            for k in item.keys():
                os.makedirs(os.path.join(key, k))



