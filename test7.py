from os import listdir, path, getcwd

folder =

# полный путь к файлам с расширениями .py
py_f = [path.join(getcwd(), item) for item in listdir() if item.endswith(".py")]
print(py_f)