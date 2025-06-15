from typing import List

import requests

url = "https://randomuser.me/api/"
response =requests.get(url)
print(response)
print(type(response))
print(response.text)

data=response.json()
user=data['results'][0]
print(user)

print(f'osoba:{user['name']}')
print(f'imie:{user['name']['first']}')
print(f'nazwisko:{user['name']['last']}')
print(f'telefon: {user['phone']}')

user_name=user['name']['first']
user_name_last=user['name']['last']
file_name= f"{user_name}_{user_name_last}.jpg"
print(file_name)
photo_url=user['picture']['large']
print(f'link do zdjecia: {photo_url}')

response_photo=requests.get(photo_url)
print(response_photo)
with open(file_name, "wb") as f:
    f.write(response_photo.content) # content to cialo tego obrazka gdzei obiekt response przechowuje dane
print("Zdjecie zostalo zapsiane ")