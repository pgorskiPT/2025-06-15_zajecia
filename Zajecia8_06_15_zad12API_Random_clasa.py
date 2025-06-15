from typing import Dict
import requests
from pydantic import BaseModel

# Pobranie danych z API
url = "https://randomuser.me/api/"
response = requests.get(url)
data = response.json()["results"][0]  # Pobranie pierwszego użytkownika

# Definicja modeli w klasach
class Name(BaseModel):
    title: str
    first: str
    last: str

class Picture(BaseModel):
    large: str
    medium: str
    thumbnail: str

class User(BaseModel):
    name: Name
    phone: str
    email: str
    picture: Picture

user_data = User(**data)

print(user_data)
print(50*'=')

print(f"Imię: {user_data.name.first}")
print(f"Nazwisko: {user_data.name.last}")
print(f"Tytuł: {user_data.name.title}")
print(f"Telefon: {user_data.phone}")
print(f"E-mail: {user_data.email}")
print(f"Zdjęcie (duży format): {user_data.picture.large}")
print(f"Zdjęcie (średni format): {user_data.picture.medium}")
print(f"Zdjęcie (miniatura): {user_data.picture.thumbnail}")
print(50*'=')

# ustawianie pliku z danych
file_name = f"{user_data.name.first}_{user_data.name.last}.jpg"
print(f"Nazwa pliku: {file_name}")

# Pobranie zdjęcia
response_photo = requests.get(user_data.picture.large)
print(50*'=')

# Zapisanie zdjęcia do pliku
with open(file_name, "wb") as f:
    f.write(response_photo.content)
print(f"Zdjęcie zapisane jako: {file_name}")

