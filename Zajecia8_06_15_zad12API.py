from typing import List, Dict

import requests as re
from pydantic import  BaseModel

url= "https://restcountries.com/v3.1/name/Poland"
response =re.get(url)
print(response)

data=response.json()[0]
print(type(data))


print(f"Oficjalna nazwa: {data['name']['official']}")
print(f"Stolica: {data['capital'][0]}") # zwraca wartosc z listy
print(f"Stolica: {data['capital']}") # zwraca liste
print(f"Region: {data['region']}, Podregion: {data['subregion']}")
print(f"Populacja: {data['population']}")
print(f"Waluta: {data['currencies']['PLN']['name']} ({data['currencies']['PLN']['symbol']})")
print(f"Język urzędowy: {', '.join(data['languages'].values())}")
print(f"Flaga: {data['flags']['png']}")
print(f"Mapa Google: {data['maps']['googleMaps']}")

print(30*'=')
class Pol(BaseModel):
    official:str

class NativeName (BaseModel):
    pol: Pol

class Name (BaseModel):
    common : str
    official:str
    nativeName: NativeName #Dict[str, dict]

class CountryInfo(BaseModel):
    name: Name
    capital: List[str]
    population: int

country_data =[CountryInfo(**data) for data in response.json()]
for country in country_data:
    print (country)
