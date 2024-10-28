import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '0b47e5ec5086ea7aa69f02906e8b5eb9'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '7259'

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["name"] == 'hihi'

@pytest.mark.parametrize('key, value' , [('name','hihi'),('trainer_id', TRAINER_ID),('id' , '117714')])
def test_parametrize(key, value):
    response_parametrize = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_parametrize.json()["data"][0][key] == value