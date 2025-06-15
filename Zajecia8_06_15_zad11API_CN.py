#skorzystac z api chuck norris
#https://api.chucknorris.io/



import requests

url = "https://api.chucknorris.io/jokes/random"
response_op = requests.options(url)
response_data = requests.get(url)
response_head = requests.head(url)

dane=response_data.json()
#
# print(response_data.json()["value"])
# print(30*'=')
# print(type(response_data))
# print(response_data)
# print(30*'=')
#
# print(type(response_op))
# print(response_op)
# print(30*'=')
#
# print(response_head.headers)
#
#
# print(30*'=')
# methods = ["GET", "POST", "OPTIONS", "HEAD"]
# for method in methods:
#     response = requests.request(method, url)
#     print(f"{method}: {response.status_code}")
#
#
# print(30*'=')
# headers = response_data.json().get("response_headers", [])
# print("\n".join(headers))

print(dane)
print(dane.keys())
from pydantic import  BaseModel
class Joke(BaseModel):
    categories: list
    created_at : str
    icon_url :str
    id:str
    updated_at :str
    url:str
    value:str
joke=Joke(**dane)
print(30*'=')
print(joke)
print(30*'=')
print(joke.value)
print(30*'=')
print(joke.url)
