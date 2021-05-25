from requests import get, utils

response = utils.get_unicode_from_response(get("http://www.cbr.ru/scripts/XML_daily.asp"))

def currency(code):
    content = response.split("<Valute ID=")
    for i in content:
        if code.upper() in i:
            return float(i.replace("/", "").split("<Value>")[-2].replace(",", "."))

print(currency(input("Введите код валюты: ")))