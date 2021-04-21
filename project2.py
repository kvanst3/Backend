import requests

cont = True

while cont:
    pokesearch = input("Which pokemon would you like to browse?").lower()
    pokerequest = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokesearch}")
    if pokerequest.status_code == 200:
        pokerequest = pokerequest.json()
        print("Pokemon name:\t", pokesearch)
        print("Pokemon type:\t", pokerequest['types'][0]['type']['name'])
        print("Pokemon weight:\t", pokerequest['weight'])
        for i in range(1, 6):
            print(f"Move {i}:\t", pokerequest['moves'][i]['move']['name'])
        if input("Would you like to browse another pokemon? [y/n]") == 'n':
            cont = False
    else:
        print("Pokemon not found")
