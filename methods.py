# methods.py

import requests
from utils import *

headers = {
        'Authorization': f'Bearer {token}'
    }


def agent_info():
    response = get_api(agent_url, headers= headers)
    return response


def new_game():
    print("\n---------------NEW GAME-----------------")
    response = get_api(agent_url, headers= headers)
    print(f'Agent {response['data']['symbol']}: Activated')
    print(agent_info())
    return


# HQ waypoint information
# X1 is the sector, X1-MZ93 is the system, and X1-MZ93-A1 is the waypoint
def hq_waypoint(agent_info):
    print("\n---------------HQ-----------------")
    for code in agent_info:
        headquarters_code = agent_info["data"]["headquarters"]
        return headquarters_code


# Get current waypoint data
def get_planet_data(system, waypoint):
    print("\n---------------PLANT INFO-----------------")
    url = f'https://api.spacetraders.io/v2/systems/{system}/waypoints/{waypoint}'
    response = get_api(url)
    return response


# Get contract information
def get_contracts():
    print("\n---------------CONTRACTS-----------------")
    contract_info = get_api(contracts_url, headers)
    return contract_info


# Negotiate contract (reset expired contracts)
def negotiate_contract():
    response = requests.get(ships, headers)
    agent_info = response.json()
    ship_symbol = agent_info['data']['symbol']

    url = f'https://api.spacetraders.io/v2/my/ships/{ship_symbol}/negotiate/contract'
    data = post_api(url, headers)
    print(data)
    return data


# Acccept contract
def accept_contract():
    contract_info = get_api(contracts_url, headers)
    contract_id = contract_info['data'][0]['id']

    url = f'https://api.spacetraders.io/v2/my/contracts/{contract_id}/accept'
    data = post_api(url, headers)

    print(f'Contract [{contract_id}]: Accepted')
    return


# Ships
def ship_info():
    response = get_api(ships, headers)
    return response


# Locate shipyards
def shipyards(system):
    url = f'https://api.spacetraders.io/v2/systems/{system}/waypoints?traits=SHIPYARD'
    response = get_api(url, headers)
    return response


def shipyard_loc(system):
    print("\n---------------SHIPYARDS-----------------")
    url = f'https://api.spacetraders.io/v2/systems/{system}/waypoints?traits=SHIPYARD'
    response = get_api(url, headers= headers)
    symbols = [item['symbol'] for item in response['data']]
    return symbols


# Ships for sale
def ships_for_sale(system):
    print("\n---------------SHIPS FOR SALE-----------------")
    url = f'https://api.spacetraders.io/v2/systems/{system}/waypoints?traits=SHIPYARD'
    response = get_api(url, headers= headers)
    symbols = [item['symbol'] for item in response['data']]
    for location in symbols:
        system_symbol = location[:7]
        url = f'https://api.spacetraders.io/v2/systems/{system_symbol}/waypoints/{location}/shipyard'
        response = get_api(url, headers= headers)
        print(response)


# Orbitals
def get_orbitals(planet_data):
    print("\n---------------PLANET ORBITALS-----------------")
    orbital_list = []
    for trait in planet_data["data"]["orbitals"]:
        orbital_list.append(trait["symbol"])
    return orbital_list


# Planet Traits
def get_planet_traits(planet_data):
    print("\n---------------PLANET TRAITS-----------------")
    trait_list = []
    for trait in planet_data["data"]["traits"]:
        trait_list.append(trait["symbol"])
    return trait_list


# Purchase ship
def purchase_ship(waypoint_symbol, ship_type):
    print("\n---------------NEW SHIP-----------------")
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }
    data = {
        "shipType": f"{ship_type}",
        "waypointSymbol": f'{waypoint_symbol}'
    }
    
    response = post_api(purchase_ship_url, headers, data)
    print(response)
