import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '0b47e5ec5086ea7aa69f02906e8b5eb9'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}

body_create = {
    "name": "hihi",
    "photo_id": 1
}

response_create = requests.post(url = f'{URL}C', headers = HEADER, json = body_create)
print(response_create.text)

message = response_create.json()['message']
print(message)