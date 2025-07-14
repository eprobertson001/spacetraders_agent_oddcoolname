import requests

token = 'add_assigned_token_here_from: https://spacetraders.io/quickstart/new-game'
headers = {
        'Authorization': f'Bearer {token}'
    }

base_url = 'https://api.spacetraders.io/v2'
contracts_url = 'https://api.spacetraders.io/v2/my/contracts'
agent_url = 'https://api.spacetraders.io/v2/my/agent'
ships = 'https://api.spacetraders.io/v2/my/ships'
purchase_ship_url = 'https://api.spacetraders.io/v2/my/ships'


# GET function: Make a GET request to a public API
# 1 arguement: API path
def get_api(path, headers=None):
    if headers:
        response = requests.get(path, headers= headers)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print("Check 1. Failed to retrieve data. Status code: ", response.status_code)
    else:
        response = requests.get(path)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print("Check 2. Failed to retrieve data. Status code: ", response.status_code) 


# POST function: Make a POST request to a public API
def post_api(path, headers=None, json=None):
    if headers:
        response = requests.post(path, headers= headers)
        if response.status_code == 200:
            response = response.json()
            print("check 3")
            print(response.status_code)
            return response
        else:
            print(" Check 5. Failed to retrieve data. Status code: ", response.status_code)
    else:
        response = requests.post(path)
        if response.status_code == 200:
            print("check 4")
            print(response.status_code)
            response = response.json()
            return response
        else:
            print(" Check 6. Failed to retrieve data. Status code: ", response.status_code)

    if json:
        response = requests.post(path, headers= headers, json= json)
        if response.status_code == 200:
            respons = response.json()
            print("check 7")
            print(response.status_code)
            return response
        else:
            print(" Check 8. Failed to retrieve data. Status code: ", response.status_code)
    else:
        response = requests.post(path, headers= headers)
        if response.status_code == 200:
            print("check 9")
            print(response.status_code)
            response = response.json()
            return response
        else:
            print(" Check 10. Failed to retrieve data. Status code: ", response.status_code)


# PUT function: Make a PUT request to a public API
# 2 arguements: API path and data to be updated
def put_api(path, data):
    response = requests.put(path, json= data)

    if response.status_code == 200:
        put_status= response.json()
        print("200: update complete")
        return put_status
    else:
        print("Failed to update data", response.status_code)
