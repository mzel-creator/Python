from datetime import date
from requests import get, utils

response = utils.get_unicode_from_response(get("http://www.cbr.ru/scripts/XML_daily.asp"))

def currency(code):
    content = response.split("<Valute ID=")
    d, m, y, = content[0].split('"')[-4].split(".")

    for i in content:
        if code.upper() in i:
            print(date(year=int(y), month=int(m), day=int(d)), end=", ")
            return float(i.replace("/", "").split("<Value>")[-2].replace(",", "."))

print(currency("usd"))
print(currency("eur"))
