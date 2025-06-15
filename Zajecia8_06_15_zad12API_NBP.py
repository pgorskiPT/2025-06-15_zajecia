from typing import List

import requests
from pydantic import BaseModel
url= "https://api.nbp.pl/api/exchangerates/rates/A/EUR/?format=json"

response=requests.get(url)
print(response)
print(response.text)
print(30*'=')
table =response.json()
print(table)
for key, value in table.items():
    print(f"{key}: {value}")
print(type(table))

print(30*'=')
print(f"""
Kurs waluty: {table["currency"]}
na dzien: {table["rates"][0]['effectiveDate']}zł
wynosi: {table["rates"][0]['mid']}zł
""")

print(30*'=')

# class CurrencyInfo(BaseModel):
#     table: str
#     currency: str
#     code: str
#     rates: List["Rate"]# Rate musi byc wczensiej zdefinowana jesli nie to powinnismy wpisac Rate w "Rate"

class Rate(BaseModel):
    no: str
    effectiveDate: str
    mid: float

class CurrencyInfo(BaseModel):
    table: str
    currency: str
    code: str
    rates: List[Rate]# Rate musi byc wczensiej zdefinowana jesli nie to powinnismy wpisac Rate w "Rate"

currency_data = CurrencyInfo(**table)

print(currency_data)
print(30*'=')
print(f"Kod waluty: {currency_data.code}")
print(f"Nazwa waluty: {currency_data.currency}")
print(f"Kurs na dzień {currency_data.rates[0].effectiveDate}: {currency_data.rates[0].mid}")
#=============================================
#robimy wariant dla wartosci w Decimal oraz zamias str uzywamy datatime dla daty

print(30*'=')
from decimal import Decimal
from datetime import datetime

class Rate1(BaseModel):
    no: str
    effectiveDate: datetime
    mid: Decimal

class CurrencyInfo1(BaseModel):
    table: str
    currency: str
    code: str
    rates: List[Rate1]# Rate musi byc wczensiej zdefinowana jesli nie to powinnismy wpisac Rate w "Rate"

currency_data = CurrencyInfo1(**table)

print(currency_data)
print(30*'=')
print(f"Kod waluty: {currency_data.code}")
print(f"Nazwa waluty: {currency_data.currency}")
print(f"Kurs na dzień {currency_data.rates[0].effectiveDate}: {currency_data.rates[0].mid}")

print(30*'=')
effectiveDate= currency_data.rates[0].effectiveDate
formated_date = effectiveDate.now().strftime("%d/%m/%Y")
print(formated_date)


print(f"Kod waluty: {currency_data.code}")
print(f"Nazwa waluty: {currency_data.currency}")
print(f"Kurs na dzień {formated_date}: {currency_data.rates[0].mid}")