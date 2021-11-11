import math
from random import randrange, uniform
from colors import *
import numpy as np

def plot_line(x0, y0, x1, y1, wd):
   dx = abs(x1-x0)
   sx = -1
   if x0 < x1:
       sx = 1
   # sx = x0 < x1 ? 1 : -1
   dy = abs(y1-y0)
   # sy = y0 < y1 ? 1 : -1
   sy = -1
   if y0 < y1:
       sy = 1
   err = dx-dy #, e2, x2, y2
   # ed = dx+dy == 0 ? 1 : sqrt(float(dx*dx)+float(dy*dy))
   ed = math.sqrt(float(dx*dx)+float(dy*dy))
   if dx+dy == 0:
       ed = 1
   points = []
   wd = (wd+1)/2
   while(True):
        #print("1")
        #wd = (wd+1)/2
        # setPixelColor(x0,y0,max(0,255*(abs(err-dx+dy)/ed-wd+1)));
        points.append((x0, y0))
        e2 = err
        x2 = x0
        if 2*e2 >= -dx:
            e2 += dy
            y2 = y0
            while(True):
                #print("2")
                #e2 += dy
                #y2 = y0
                if not ((e2 < ed*wd) and (y1 != y2 or dx > dy)):
                    break
                # setPixelColor(x0, y2 += sy, max(0,255*(abs(e2)/ed-wd+1)));
                y2 += sy
                points.append((x0, y2))
                e2 += dx
            if x0 == x1:
                break
            e2 = err
            err -= dy
            x0 += sx
        if 2*e2 <= dy:
            e2 = dx-e2
            while(True):
                #print("3")
                #e2 = dx-e2
                if not ((e2 < ed*wd) and (x1 != x2 or dx < dy)):
                    break
                x2 += sx
                points.append((x2, y0))
                # setPixelColor(x2 += sx, y0, max(0,255*(abs(e2)/ed-wd+1)));
                e2 += dy
            if y0 == y1:
                break
            err += dx
            y0 += sy
   return points
  
def get_random_scale():
    fixed_scale = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
    light_fixed_scale = (1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2)
    hard_fixed_scale = (1, 1.3, 1.5, 1.7, 1.9, 2.1, 2.3, 2.5, 2.7, 3)
    scales =[]
    scales.append(fixed_scale)
    scales.append(light_fixed_scale)
    scales.append(hard_fixed_scale)
    i = randrange(0,3)
    if i == 0:
        print("Scale: Fixed scale")
    elif i == 1:
        print("Scale: Light scale")
    else:
        print("Scale: Hard scale")
    scale = scales[i]
    return scale
   
cnt = 0
visited = np.zeros((800,800)) 

def count_water_pixels(strt, graph):

    global cnt 
    start = (int(strt[0]), int(strt[1]))
    if cnt >=400:
        return
    steps = [(0,1),(1,0),(0,-1),(-1,0)]
    if visited[start[0]][start[1]] != 1 and graph[start[0]][start[1]]<0:
        #points.append(start)
        cnt +=1
        #print(str(graph[start[0]][start[1]])+" count: "+str(cnt))
        visited[start[0]][start[1]] = 1
    else:
        return
    if start[0]==0 or start[0]==799 or start[1]==0 or start[1] == 799:
        return
    for step in steps:
        count_water_pixels((start[0]+step[0],start[1]+step[1]), graph)

def set_cnt():
    global cnt
    cnt = 0
def get_biome(e, m, water_level, temperature_factor, mountains_factor, sea_level_factor):
        water_levell = water_level + sea_level_factor           
        if e<water_levell:
            if m > temperature_factor+0.88:
                return ICE
            return WATER

        if e<water_levell+0.1:
            if m<temperature_factor:
                return BEACH_HOT
            if m<temperature_factor+0.8:
                return BEACH
            if m<temperature_factor+0.85:
                return BEACH_COLD
            return SNOW       

        if e>water_level+3.2-mountains_factor:
            if m < temperature_factor:
                return DESERT_MOUNTAINS_8
            if m < temperature_factor+ 0.8:
                return MOUNTAINS_8
            else:
                return COLD_MOUNTAINS_8

        if e>water_level+2.8-mountains_factor:
            if m < temperature_factor:
                return DESERT_MOUNTAINS_7
            if m < temperature_factor+ 0.8:
                return MOUNTAINS_7
            else:
                return COLD_MOUNTAINS_7

        if e>water_level+2.5-mountains_factor:
            if m < temperature_factor:
                return DESERT_MOUNTAINS_6
            if m < temperature_factor+ 0.8:
                return MOUNTAINS_6
            else:
                return COLD_MOUNTAINS_6

        if e>water_level+2-mountains_factor:
            if m < temperature_factor:
                return DESERT_MOUNTAINS_5
            if m < temperature_factor+ 0.8:
                return MOUNTAINS_5
            else:
                return COLD_MOUNTAINS_5

        if e>water_level+1.6-mountains_factor:
            if m < temperature_factor:
                return DESERT_MOUNTAINS_4
            if m < temperature_factor+ 0.8:
                return MOUNTAINS_4
            else:
                return COLD_MOUNTAINS_4

        if e>water_level+1.4-mountains_factor:
            if m < temperature_factor:
                return DESERT_MOUNTAINS_3
            if m < temperature_factor+ 0.8:
                return MOUNTAINS_3
            else:
                return COLD_MOUNTAINS_3

        if e>water_level+1.3 - mountains_factor:
            if m < temperature_factor:
                return DESERT_MOUNTAINS_OUTLINE
            if m < temperature_factor+ 0.8:
                return MOUNTAINS_OUTLINE
            else:
                return SNOW

        if e>water_level+1 :#- mountains_factor
            if m < temperature_factor:
                return DESERT_MOUNTAINS_2
            if m < temperature_factor+ 0.8:
                return MOUNTAINS_2
            else:
                return COLD_MOUNTAINS_2

        if e>water_level+0.9 :#- mountains_factor
            if m < temperature_factor:
                return DESERT_MOUNTAINS_1
            if m < temperature_factor+ 0.8:
                return MOUNTAINS_1
            else:
                return COLD_MOUNTAINS_1

        if e>water_level+0.5:
            if m < temperature_factor:
                return DESERT
            if m < temperature_factor +0.85:
                return FOREST
            return SNOW

        if e>water_levell+0.2:
            if m < temperature_factor:
                return DESERT            
            if m < temperature_factor+0.8:
                return GRASS
            return SNOW

        if m < temperature_factor:
            return DESERT
        if m < temperature_factor+0.8:
            return GRASS        
        return SNOW

def get_civilizations_color(e, m, water_level, temperature_factor, mountains_factor, sea_level_factor, country_color):
        water_levell = water_level + sea_level_factor           
        if e<water_levell:
            return WATER
            # if m > temperature_factor+0.88:
            #     return ICE
            # return WATER

        if e<water_levell+0.1:
            if country_color == (255, 0, 0):
                return RED_1
            if country_color == (0, 0, 204):
                return BLUE_1
            if country_color == (70, 70, 70):
                return GREEN_1
            return PINK_1      

        # if e>water_level+3.2-mountains_factor:
        #     if country_color == (255, 0, 0):
        #         return RED_1
        #     if country_color == (0, 0, 204):
        #         return (0, 0, 204)
        #     return (153, 0, 204) 

        # if e>water_level+2.8-mountains_factor:
        #     if country_color == (255, 0, 0):
        #         return RED_1
        #     if country_color == (0, 0, 204):
        #         return (0, 0, 204)
        #     return (153, 0, 204) 

        if e>water_level+2.5-mountains_factor:
            if country_color == (255, 0, 0):
                return RED_8
            if country_color == (0, 0, 204):
                return BLUE_8
            if country_color == (70, 70, 70):
                return GREEN_8
            return PINK_8  

        if e>water_level+2-mountains_factor:
            if country_color == (255, 0, 0):
                return RED_7
            if country_color == (0, 0, 204):
                return BLUE_7
            if country_color == (70, 70, 70):
                return GREEN_7
            return PINK_7  

        if e>water_level+1.6-mountains_factor:
            if country_color == (255, 0, 0):
                return RED_6
            if country_color == (0, 0, 204):
                return BLUE_6
            if country_color == (70, 70, 70):
                return GREEN_6
            return PINK_6  

        if e>water_level+1.4-mountains_factor:
            if country_color == (255, 0, 0):
                return RED_5
            if country_color == (0, 0, 204):
                return BLUE_5
            if country_color == (70, 70, 70):
                return GREEN_5
            return PINK_5  

        if e>water_level+1.3 - mountains_factor:
            if country_color == (255, 0, 0):
                return RED_4
            if country_color == (0, 0, 204):
                return BLUE_4
            if country_color == (70, 70, 70):
                return GREEN_4
            return PINK_4  

        if e>water_level+1 :#- mountains_factor
            if country_color == (255, 0, 0):
                return RED_3
            if country_color == (0, 0, 204):
                return BLUE_3
            if country_color == (70, 70, 70):
                return GREEN_3
            return PINK_3  

        if e>water_level+0.9 :#- mountains_factor
            if country_color == (255, 0, 0):
                return RED_2
            if country_color == (0, 0, 204):
                return BLUE_2
            if country_color == (70, 70, 70):
                return GREEN_2
            return PINK_2  

        if e>water_level+0.5:
            if country_color == (255, 0, 0):
                return RED_2
            if country_color == (0, 0, 204):
                return BLUE_2
            if country_color == (70, 70, 70):
                return GREEN_2
            return PINK_2  

        if e>water_levell+0.2:
            if country_color == (255, 0, 0):
                return RED_2
            if country_color == (0, 0, 204):
                return BLUE_2
            if country_color == (70, 70, 70):
                return GREEN_2
            return PINK_2  

        if country_color == (255, 0, 0):
            return RED_2
        if country_color == (0, 0, 204):
            return BLUE_2
        if country_color == (70, 70, 70):
            return GREEN_2
        return PINK_2 
