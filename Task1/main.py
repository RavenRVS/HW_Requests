import requests

def cleverest_hero(list_hero):
  url = "https://akabab.github.io/superhero-api/api/all.json"
  resp = requests.get(url).json()
  hero_intelligence_list = {}
  for name_hero in list_hero:
    for first_hero in resp:
      if first_hero['name'] == name_hero:
        hero_intelligence_list[first_hero['name']] = first_hero['powerstats']['intelligence']
  sorted_heros = sorted(hero_intelligence_list.items(), key = lambda x: x[1], reverse=True)
  print(f'{sorted_heros[0][0]} самый умный герой из списка. Его интеллект равен {sorted_heros[0][1]}')

My_list_hero = cleverest_hero(['Thanos', 'Hulk', 'Captain America'])