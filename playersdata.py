import requests
import json

page_number = 0
while True:
    page_number += 1
    query = {'page': '1', 'per_page': '25'}

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
    file = open('nbaplayers.txt', 'w')
    file.write('Name,Surname,Height(inches),Height(feet)\n')
    allPlayers = len(playersData['data'])
    complete_data = ''

    for player in range(0, allPlayers):
        item = playersData['data'][player]
        if item['first_name'] is not None:
            complete_data += str(item['first_name'])
        complete_data += ','
        if item['last_name'] is not None:
            complete_data += str(item['last_name'])
        complete_data += ','
        if item['height_inches'] is not None:
            complete_data += str(item['height_inches'])
        complete_data += ','
        if item['height_feet'] is not None:
            complete_data += str(item['height_feet'])
        complete_data += '\n'
    file.write(complete_data)
    break
file.close()
