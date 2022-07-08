from pprint import pprint

import requests

def most_intelligence():
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    response = requests.get(url=url)

    if response.status_code != 200:
        print(response)
    superheroes = response.json()

    name = None
    intelligence = 0
    for superhero in superheroes:
        if superhero['name'] == 'Hulk' or superhero['name'] == 'Captain America' or superhero['name'] == 'Thanos':
            powerstats = superhero['powerstats']
            if powerstats['intelligence'] > intelligence:
                name = superhero['name']
                intelligense = powerstats['intelligence']
    return name


if __name__ == '__main__':
    print(f'Самый умный из трех героев - {most_intelligence()}')
