import math
import random

cities = [[(100,120),(200,200)],[(250,250),(101,101)]]

roads = []
flat_list = [item for sublist in cities for item in sublist]
def get_closest_cities(city, cities,n):
        cities_by_distance = sorted(cities, key=lambda x: math.sqrt((city[0] - x[0])**2+(city[1] - x[1])**2), reverse=False)
        return cities_by_distance[:n]

for city in flat_list:
    n = random.randint(1,3)
    n = 2
    closest_cities = get_closest_cities(city,flat_list,n)
    closest_cities = closest_cities[1:]
    for cc in closest_cities:
        duplicate = False
        if city[0]<cc[0]:
            road = [city,cc]
        else:
            road = [cc, city]
        for r in roads:
            if r == road:
                duplicate = True
                break        
        if duplicate == False:
            roads.append(road)

print(roads)