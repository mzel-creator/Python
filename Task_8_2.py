import re

RE_NAME = re.compile(r'([\w\.\+\:\/]+)')

def parcer_log(str_line):
    log_list = RE_NAME.findall(str_line) # разбивка на блоки, findall возвращает список
    print((log_list[0], log_list[1] + log_list[2], log_list[4], log_list[6], log_list[7]))

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        parcer_log(line)
