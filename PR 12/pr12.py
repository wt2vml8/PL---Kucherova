#type:ignore
import json
import requests
from pprint import pprint
# Имя пользователя github
username = 'openshift'
# url для запроса
url = f"https://api.github.com/users/{username}"
# делаем запрос и возвращаем json
user_data1 = requests.get(url).json()
# довольно распечатать данные JSON
pprint(user_data1)
c1 = json.dumps(user_data1)
print('-'*50)
pprint(c1)
user_data = json.loads(c1)
print('-'*50)
pprint(user_data)
info = {
        'company'   : (user_data["company"]),
        'created_at': (user_data["created_at"]),
        'email'     : (user_data["email"]),
        'id'        : (user_data["id"]),
        'name'      : (user_data["name"]),
        'url'       : (user_data["url"])
        }
pprint(info)
print('-'*50)
with open('Json.txt', 'w') as file_json:
  json.dump(info,file_json)