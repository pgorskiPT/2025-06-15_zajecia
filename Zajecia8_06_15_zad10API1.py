"""
REST API (Representational State Transfer API) to styl architektoniczny używany
do tworzenia interfejsów komunikacji między aplikacjami za pomocą protokołu HTTP.
REST API pozwala na wysyłanie żądań i odbieranie odpowiedzi w formacie JSON lub XML,
co umożliwia łatwą wymianę danych między systemami.
🔹 Jak działa REST API?
REST API opiera się na operacjach CRUD (Create, Read, Update, Delete),
które są realizowane przez metody HTTP:
GET – pobiera dane z serwera.
POST – tworzy nowy zasób na serwerze.
PUT – aktualizuje istniejący zasób.
DELETE – usuwa zasób.

Oto podstawowe metody HTTP, które są używane w komunikacji z serwerem:
🔹 GET – Pobiera zasoby z serwera (np. stronę internetową, dane z API).
🔹 POST – Tworzy nowy zasób na serwerze (np. dodawanie użytkownika, wysyłanie formularza).
🔹 PUT – Aktualizuje istniejący zasób lub tworzy nowy, jeśli nie istnieje.
🔹 PATCH – Częściowa aktualizacja zasobu (np. zmiana jednego pola w bazie danych).
🔹 DELETE – Usuwa zasób z serwera.
🔹 OPTIONS – Sprawdza dostępne metody dla danego zasobu (np. jakie operacje są dozwolone).
🔹 HEAD – Podobny do GET, ale pobiera tylko nagłówki, bez zawartości odpowiedzi.
🔹 TRACE – Testuje ścieżkę żądania i zwraca informacje o przebytej trasie.
🔹 CONNECT – Tworzy tunel do serwera, często używane dla połączeń HTTPS.
"""
from typing import List

# import requests
#
# url = "https://v2.api.raporty.pse.pl/app/home"
# response = requests.options(url)
#
# # Wyświetlenie każdego nagłówka w osobnej linii
# for key, value in response.headers.items():
#     print(f"{key}: {value}")



# import requests
#
# url = "http://api.open-notify.org/astros.json"
# response = requests.options(url)
#
# # Wyświetlenie każdego nagłówka w osobnej linii
# for key, value in response.headers.items():
#     print(f"{key}: {value}")



# import requests
#
# url = "http://api.open-notify.org/astros.json"
# response = requests.get(url)
#
# # Pobranie danych JSON
# data = response.json()
#
# # Wyświetlenie każdego elementu w oddzielnej linii
# for key, value in data.items():
#     print(f"{key}: {value}")


# import requests
#
# url = "http://api.open-notify.org/astros.json"
# response = requests.get(url)
#
# # Pobranie danych JSON
# data = response.json()
#
# # Wyświetlenie każdego klucza i wartości w oddzielnych wierszach
# for key, value in data.items():
#     print(f"{key}:")
#
#     # Jeśli wartość to lista (np. lista astronautów), iteruj przez nią
#     if isinstance(value, list):
#         for item in value:
#             print(f"  - craft: {item['craft']}")
#             print(f"    name: {item['name']}")
#     else:
#         print(f"  {value}")


import requests

url = "http://api.open-notify.org/astros.json"
response = requests.get(url)
print(response) # zwraca kod odpwoeidzi ze strony 2xx - oki;
# 3xx -przekierowania, warningi;  4xx - beldy zapytania; 5xx bledy serwera
print(response.text)
print(type(response.text))

# trzeba jsona zamienic na slownik

# Pobranie danych JSON
response_data = response.json()
print(type(response_data))
print(response_data)


# astronauts = response.json().get("people", [])
#
# for person in astronauts:
#     print(f"Imię: {person['name']}, Statek: {person['craft']}")


people_list=response_data['people']
for i in people_list:
    print(i)
print(30*'=')
print (response.json().get("people", []))

print(30*'=')
print ( [person['name'] for person in response.json().get("people", [])])

print(30*'=')
print("\n".join([person['name'] for person in response.json().get("people", [])]))

print(30*'=')
from pydantic import BaseModel # biblioteka ktora pozwala parsowac json na obiekty

class Astros(BaseModel):
    craft: str
    name: str

class AstroData(BaseModel):
    #people: list
    people: List[Astros]
    number: int
    message: str


data =AstroData(**response_data)
print(data)

print (data.number)
print(data.message)
print(30*'=')

for p in data.people:
    print(f'{p.name=}, {p.craft=}')

print(30*'=')

for p in data.people:
    #print(p)
    print(p.__class__.__name__)
    print(f'{p.name} {p.craft}')