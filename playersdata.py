import requests
import json
file = open('nbaplayers.txt', 'w')

while True:
    i = 0
    i = i + 1
    query = {'page': str(i), 'per_page':'25', 'search': ''}

    #Reads API and checks if there're no errors
    try:
        response_API = requests.get('https://www.balldontlie.io/api/v1/players', timeout=50, params=query)
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


    #Uploading data to file:

    #Data about players:
    allPlayers = len(playersData['data'])

    for player in range(0, allPlayers):
        item = playersData['data'][player]
        if item['first_name'] != None:
            file.write('Name: ')
            file.writelines(str(item['first_name']))
        if item['last_name'] != None:
            file.write(' Surame: ')
            file.writelines(str(item['last_name']))
        if item['height_inches'] != None:
            file.write(' Height(inches): ')
            file.writelines(str(item['height_inches']))
        if  item['height_feet'] != None:
            file.write(' Height(feet): ')
            file.writelines(str(item['height_feet']))
        file.write('\n')
file.close()
        
   






   


   


