from world_map import WorldMap
from start_data_object import StartDataObject
from helper import *
from random import randrange, uniform
import numpy as np
import time



finished = False    
world_map = None
add_rivers = False
heights = []

def main(start_data_object):
    global finished
    global world_map
    global add_rivers
    global heights
    finished = False
    if start_data_object.is_rivers == False:
        add_rivers = True
    # for i in range(0,50):
    #     try:
    print("###########################################")
    # size = (800, 800)
    # elevation_seed_index = randrange(1,2)
    # temperature_seed_index = randrange(1,10)
    # elevation_seed = np.loadtxt("elevation_seeds/seed"+str(elevation_seed_index)+".txt")
    # temperature_seed = np.loadtxt("temperature_seeds/seed"+str(temperature_seed_index)+".txt")
    # scale = get_random_scale()           
    # is_rivers = True
    # civilisations = False
    # water_level = 0.3
    # temperature_factor = uniform(-0.6,0.8) #-0.6 |snieg| -0.1 |trawa| 0.7 piach
    # islands_number = randrange(1,10)
    # heights = None
    #custom config
    #fixed = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
    #light_fixed = (1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2)
    # scale = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
    #temperature_factor = 0.7
    # islands_number = 10
    # heights = [(476, 246), (528, 741), (544, 375), (697, 258), (204, 230), (395, 280), (267, 263), (478, 697), (713, 515)]
    # is_rivers = True
    # scale = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
    # water_level = 0.4
    ##############

    print("Temperature: "+str(start_data_object.temperature_factor))
    print("Mountains: "+str(start_data_object.mountains_factor))
    print("Sea level: "+str(start_data_object.sea_level_factor))
    print("Urbanization level: "+str(start_data_object.urbanization_level_factor))        
    # start_data_object = StartDataObject(size, elevation_seed, temperature_seed, scale, is_rivers, 
    #     civilisations, water_level, temperature_factor, islands_number, heights)
    start = time.time()
    world_map = WorldMap(start_data_object)
    world_map.generate()
    world_map.draw_map()
    finished = True
    heights = world_map.heights
    end = time.time()
    print("Total generating time: "+ str(end-start) + "s")
    print("###########################################")
    # except:
    #     print("ERROR

def cancel_rivers():
    global world_map
    global finished
    finished = False
    world_map.cancel_rivers()
    finished = True

def re_draw(new_temperature, new_mountains, new_sea_level, is_rivers, selected_heights, is_civilizations, is_borders, new_urbanization,  ):
    global world_map
    global finished
    global add_rivers
    finished = False
    world_map.temperature_factor = new_temperature
    world_map.mountains_factor = new_mountains
    world_map.civilisations = is_civilizations
    redraw_civs = False
    if world_map.urbanization_level_factor != new_urbanization:
        redraw_civs = True
    world_map.urbanization_level_factor = new_urbanization
    world_map.borders = is_borders

    
    if (is_civilizations and world_map.cities == None) or redraw_civs:
        world_map.redraw_civilizations()

    if selected_heights != world_map.heights:
        world_map.cancel_islands()
        world_map.heights = selected_heights
        world_map.add_islands()
    else:
        world_map.heights = selected_heights
    
    if new_sea_level < world_map.sea_level_factor and is_rivers == True:
        world_map.sea_level_factor = new_sea_level
        world_map.cancel_rivers()
        world_map.add_rivers()
    elif new_sea_level > world_map.sea_level_factor and is_civilizations == True:
        world_map.sea_level_factor = new_sea_level
        world_map.redraw_civilizations()
    else:
        world_map.sea_level_factor = new_sea_level
    ##
    if is_rivers == False:
        world_map.cancel_rivers()
        add_rivers = True
    else:
        if add_rivers:
            world_map.add_rivers()
            add_rivers = False
    # world_map.redraw_civilizations()
    world_map.draw_map()
    finished = True

if __name__ == '__main__':
    main()


