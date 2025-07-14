import requests
from methods import *

oddcoolname_info = agent_info()

oddcoolname_hq_waypoint = hq_waypoint(oddcoolname_info)
oddcoolname_hq_system = oddcoolname_hq_waypoint[:7]
print(f'HQ Location: {oddcoolname_hq_waypoint}')

# print(ship_info())

# engineered_asteroid_url = f'https://api.spacetraders.io/v2/systems/{oddcoolname_hq_system}/waypoints?type=ENGINEERED_ASTEROID'
# asteroid_data = get_api(engineered_asteroid_url)
# print(asteroid_data)


# orbit_url = 'https://api.spacetraders.io/v2/my/ships/ODDCOOLNAME-3/orbit'
# response = post_api(orbit_url, headers = headers)
# print(response)


#Navigate
navigate_url = 'https://api.spacetraders.io/v2/my/ships/ODDCOOLNAME-1/navigate' 
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {token}'
}
data = {
    "waypointSymbol": 'X1-TG13-ZE5D'
}

nav_response = post_api(navigate_url, headers= headers, json= data)
print(nav_response)
