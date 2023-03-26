import requests
import json


#Reads API and checks if there're no errors
try:
    response_API = requests.get('https://www.balldontlie.io/api/v1/players', timeout=5, data = {'key':'value'})
    response_API.raise_for_status()
    # Code here will only run if the request is successful
except requests.exceptions.HTTPError as errh:
    print(errh)
except requests.exceptions.ConnectionError as errc:
    print(errc)
except requests.exceptions.Timeout as errt:
    print(errt)
except requests.exceptions.RequestException as err:
    print(err)


#Function to fix null values:
def fix_data(data):
    if type(data) is list:
        for i, e in enumerate(data):
            if e is None:
                data[i] = '-'
            else:
              fix_data(e)

    elif type(data) is dict:
        for k, v in data.items():
            if v is None:
                data[k] = '-'
            else:
                fix_data(v)

#Function to fix integers to strings:
def fix_intdata(data):
    if type(data) is list:
        for i, e in enumerate(data):
            if isinstance(e, int):
                data[i] = str(e)
            else:
              fix_intdata(e)

    elif type(data) is dict:
        for k, v in data.items():
            if isinstance(v, int):
                data[k] = str(v)
            else:
                fix_intdata(v)




#Reads API and opens json:
data = response_API.text 
playersData = json.loads(data)
fix_data(playersData)
fix_intdata(playersData)


#Data about players
allPlayers = len(playersData['data'])
for a in range(0, allPlayers):
    playerName = playersData['data'][a]['first_name']
    playerSurname = playersData['data'][a]['last_name']
    playerHeightI = playersData['data'][a]['height_inches']
    playerHeightF = playersData['data'][a]['height_feet']
    print('Players name: ' + playerName + ' ' + playerSurname + ' |Height inches: ' + playerHeightI + '|Height feet: ' + playerHeightF)
   
   
   


   


