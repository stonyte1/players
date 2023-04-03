import requests
import json
from datetime import datetime, timedelta


#Gets yesterdays date 
yesterday_datetime = datetime.now() - timedelta(days=1)
yesterday_date = yesterday_datetime.strftime('%Y-%m-%d')

file = open('%s.txt' % yesterday_date, 'w')

while True:
    i = 0
    i = i + 1
    query = {'page': str(i), 'per_page':'25', 'search': '', 'dates': str(yesterday_date)}

    #Reads API and checks if there're no errors
    try:
        response_API = requests.get('https://www.balldontlie.io/api/v1/stats', timeout=50, params=query)
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


    #Reads API and opens json:
    playersData = json.loads(response_API.text)

    #Data about players:
    allPlayers = len(playersData['data'])

    for player in range(0, allPlayers):
        item = playersData['data'][player]
        if item['player']['first_name'] != None:
            file.write('Name: ')
            file.writelines(str(item['player']['first_name']))
        if item['player']['last_name'] != None:
            file.write(' Surame: ')
            file.writelines(str(item['player']['last_name']))
        if item['pts'] != None:
            file.write(' Points: ')
            file.writelines(str(item['pts']))
        if  item['reb'] != None:
            file.write(' Rebound: ')
            file.writelines(str(item['reb']))
        if  item['stl'] != None:
            file.write(' Steals: ')
            file.writelines(str(item['stl']))
        file.write('\n')

file.close()
        
   






   


   


