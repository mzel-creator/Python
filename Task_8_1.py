import re

def email_parse(email_address):
    RE_email = re.compile(r'(?P<username>([\w]+))@(?P<domain>[^&]+\.\w+)', re.IGNORECASE)
    if not RE_email.match(email_address):
        raise ValueError(fr'wrong email: {email_address}')
    print(RE_email.match(email_address).groupdict())

for i in ['ivanov@mail.ru', 'petrov@gmail.com', 'sidorov@hotmail.com', 'popov@lisr.ru', 'ivanov@mail', 'petrov@gmailcom', 'sidorovhotmail.com', 'lisr.ru']:
    try:
        email_parse(i)
    except ValueError as arr:
        print(arr)