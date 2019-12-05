import requests
#r = requests.get('https://swapi.co/api/people/30/')
#print(r.json())
#starwarsguy = r.json()
#print(starwarsguy["birth_year"])
#This will call an API to find which area is sunny
#a = requests.get('https://swapi.co/api/people/30/')
#sunny_place = a.json()
#This will ask Location API for flight codes
#b = requests.get('https//swapi.co/api/planets/')
#flightcodes = b.json
#wanted_flightcode=flightcodes[sunny_place])

#CODE TO SHOW HOME PLANET OF CHARACTERS IN EMPIRE STRIKES BACK
#API REQUEST FOR EMPIRE STRIKES BACK
film= requests.get('https://swapi.co/api/films/2/')

#SHOWS LIST OF CHARACTERS IN EMPIRE
film_characters = film.json()["characters"]

#SHOWS LENGTH OF THE LIST
film_characters_length =len(film_characters)

#CREATES NEW LIST, ITERATES OVER LIST AND APPENDS NEW ONE
film_char_list = []
for i in range (0, film_characters_length):
    film_char_list.append(film_characters[i])

#SHOWS LIST OF PLANETS
planets = requests.get('https://swapi.co/api/planets/')



#for j in range(0, film_characters_length):
 #   current_char = film_char_list[j]

#Creates list, makes list of home planets
home_planet_list = []
for i in film_char_list:
    film_character_detail = requests.get(i).json()["homeworld"]
    home_planet_list.append(film_character_detail)

print(home_planet_list)

#print(list_of_planets)
#print(film_char_list)





