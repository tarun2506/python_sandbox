# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json

#sample json

userJSON = '{"First_name": "Tarun", "Last_name": "Sharma", "age": 17}'

#parse to dict
user = json.loads(userJSON)

print(user)
print(user['First_name'])

car = {'make': 'Ford', 'model': 'Mustang', 'year': 1970}

carJSON = json.dumps(car)

print(carJSON)