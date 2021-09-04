import json
import requests
from requests.exceptions import HTTPError
from pprint import pprint

# Endpoint PokeApi
POKEAPI = "https://pokeapi.co/api/v2"
URL_EVOLUTION = "evolution-chain"
URL_POKEMON = "pokemon"

# Endpoint Django
LOCAL_API = 'http://localhost:8000'
URL_CREATE_CHAIN = 'evolution-chain'
URL_CREATE_POKE = 'pokemon'
URL_CREATE_STATS = 'stats'

id_chain = 0


def get_response_api(endpoint, param):
	url = '{api}/{endpoint}/{param}'.format(
		api=POKEAPI,
		endpoint=endpoint,
		param=param
	)

	try:
		response = requests.get(url)
		response.raise_for_status()
	except HTTPError as http_err:
		print(f'HTTP error occurred: {http_err}')
	except Exception as err:
		print(f'Other error occurred: {err}')
	else:
		return response.json() # print('Success!')


def post_create_local_api(url, json):
	try:
		# headers = {'Content-type': 'application/json'}
		response = requests.post(
			url=url,
			json=json
		)
		response.raise_for_status()
	except HTTPError as http_err:
		print(f'HTTP error occurred: {http_err}')
		print(response.content)
	except Exception as err:
		print(f'Other error occurred: {err}')
		print(response.content)
	else:
		return response.json()


def get_evolution_chain(id_chain):
	pk_chain_db = None

	def recursive_chain(poke):
		poke_name = poke['species']['name']
		get_pokemon(poke_name, pk_chain_db)
		evolutions = poke['evolves_to'] # lista
		for evolve in evolutions:
			recursive_chain(evolve)
	
	json_chain = get_response_api(URL_EVOLUTION, id_chain)

	# Create chain local api
	url = '{local}/{endpoint}/'.format(
		local=LOCAL_API,
		endpoint=URL_CREATE_CHAIN
	)
	json = {'id_chain': int(id_chain)}
	created_chain = post_create_local_api(url, json)

	if created_chain:
		pk_chain_db = created_chain['id']
		recursive_chain(json_chain['chain'])
	# ==== Fin chain =========


def get_pokemon(name, pk_chain):
	json_poke = get_response_api(URL_POKEMON, name)

	# Create pokémon local api
	url = '{local}/{endpoint}/'.format(
		local=LOCAL_API,
		endpoint=URL_CREATE_POKE
	)
	json = {
		'chain': pk_chain,
		'id_pokemon': int(json_poke['id']),
		'name': json_poke.get('name'),
		'image': json_poke['sprites']['other']['official-artwork']['front_default'],
		'height': json_poke.get('height'),
		'weight': json_poke.get('weight'),
		'order': int(json_poke['order']),
	}
	created_poke = post_create_local_api(url, json)
	if created_poke:
		print('Created ==>', json_poke.get('name'))
		get_stats(json_poke.get('stats', []), created_poke['id'])
	# ==== Fin Pokémon =========


def get_stats(stats, id_poke):
	# Create stats pokémon local api
	url = '{local}/{endpoint}/'.format(
		local=LOCAL_API,
		endpoint=URL_CREATE_STATS
	)
	for stat in stats:
		json = {
			'pokemon': id_poke,
			'name': stat['stat']['name'],
			'base': stat['base_stat'],
			'effort': stat['effort']
		}
		created_stat = post_create_local_api(url, json)
	# ==== Fin Stats =========


def validate_id(id_chain):
	try:
		return int(id_chain)
	except ValueError:
		return False


def create_evolution_chain():
	id_chain = input()
	while not validate_id(id_chain):
		print('Enter a numeric value')
		id_chain = input()
	return id_chain


def _print_welcome():
	print('*'*30)
	print('***** Welcome to PokeApi *****')
	print('*'*30)
	print('Please enter the ID')
	print('ID which represents the Evolution Chain of the pokémon')


if __name__ == '__main__':
	_print_welcome()
	create = 'y'
	while create.lower() == 'y':
		id_chain = create_evolution_chain()
		chain_info = get_evolution_chain(id_chain)
		print('Create other Evolution Chain? Y/n')
		create = input()

