from itertools import count
from random import randrange, uniform, sample

from numpy.core.fromnumeric import size
import helper as hlp
from PIL import Image, ImageDraw
import math
import numpy as np
import colors


class WorldMap:
    def __init__(self, data):
        self.size = data.size
        self.elevation_map = data.elevation_seed
        self.countries_map = np.copy(data.elevation_seed)
        self.backup_rivers_map = None
        self.backup_islands_map = None
        self.temperature_map = data.temperature_seed       
        self.scale = data.scale
        self.is_rivers = data.is_rivers
        self.civilisations = data.civilisations
        self.water_level = data.water_level
        self.temperature_factor = data.temperature_factor
        self.mountains_factor = data.mountains_factor
        self.sea_level_factor = data.sea_level_factor
        self.islands_number =  data.islands_number
        self.heights = data.heights
        self.countries =  None
        self.rivers = None
        self.extra_rivers = None
        self.red_rivers = []

    def generate(self):
        self.backup_islands_map = np.copy(self.elevation_map)
        if self.heights == None or self.heights == []:
            self.heights = self.generate_islands(self.size[0], self.size[1], self.islands_number)        
        print("Heights:")
        print(self.heights)      
        self.modify_elevation_map_with_islands()          
        self.backup_rivers_map = np.copy(self.elevation_map)
        if self.is_rivers:
            #self.generate_rivers(self.size, self.elevation_map, self.water_level)
            self.generate_rivers(self.size, self.water_level, self.sea_level_factor)       
            self.make_rivers_deep(self.rivers, self.elevation_map, 3)
            #self.make_rivers_deep(self.extra_rivers, self.elevation_map, 2)
            self.thermal_erosion(self.size, self.elevation_map)
        self.countries = self.heights[0:2]
        if self.civilisations:
            self.countries = self.create_countries(self.heights, 2)
            self.create_countries_map(self.heights, self.countries) 
        print(self.countries_map)
        #self.make_rivers_deep(self.extra_rivers, self.elevation_map, 1)
        #self.hydraulic_erosion(self.size, self.elevation_map, self.rivers)
        #self.draw_map()
        
        #self.draw_map()
    def cancel_islands(self):
        self.elevation_map = np.copy(self.backup_islands_map)

    def add_islands(self):
        self.modify_elevation_map_with_islands()
        self.backup_rivers_map = np.copy(self.elevation_map)     

    def add_rivers(self):
        self.generate_rivers(self.size, self.water_level, self.sea_level_factor)       
        self.make_rivers_deep(self.rivers, self.elevation_map, 3)
        #self.make_rivers_deep(self.extra_rivers, self.elevation_map, 2)
        self.thermal_erosion(self.size, self.elevation_map)

    def cancel_rivers(self):
        self.elevation_map = np.copy(self.backup_rivers_map)

    def draw_map(self):
        img = Image.new( 'RGB', self.size, "black")
        pixels = img.load()
        draw = ImageDraw.Draw(img)
        if self.civilisations:
            for y in range(self.size[1]):
                for x in range(self.size[0]): 
                    country_index = int(self.countries_map[y][x])
                    e = self.elevation_map[y][x]
                    m = self.temperature_map[y][x]
                    pixel = hlp.get_biome(e, m, self.water_level, self.temperature_factor, self.mountains_factor, self.sea_level_factor)
                    if pixel == (24, 161, 219) or pixel == (154, 245, 234):
                        biome = pixel
                    else:
                        biome = colors.country_colors[country_index]
                    pixels[x,y] = biome
        else:
            for y in range(self.size[1]):
                for x in range(self.size[0]):
                    e = self.elevation_map[y][x]
                    m = self.temperature_map[y][x]
                    biome= hlp.get_biome(e, m, self.water_level, self.temperature_factor, self.mountains_factor, self.sea_level_factor)
                    pixels[x,y] = biome
            # if self.red_rivers != []:
            #     for red_river in self.red_rivers:
            #         draw.line(red_river, fill=(237,28,36), width=2)
        # for extra_river in self.extra_rivers:
        #     draw.line(extra_river, fill=WATER, width=3)
        #img.show()
        #img = img.save("generated_maps_22_10/"+str(self.elevation_map[0][0])+".jpg", format='JPEG', subsampling=0, quality=100 ) 
        img = img.save("image.jpg", format='JPEG', subsampling=0, quality=100 )        
        print("Finished drawing map")
        return 1
        
    def modify_elevation_map_with_islands(self):
        for y in range(self.size[1]):   
            for x in range(self.size[0]):
                temp = self.elevation_map[y][x]
                custom = self.islands_function(y, x, self.heights, self.size[0], self.scale)
                temp -= custom 
                temp = temp / (0.54 + 0.50 + 0.25+  0.13)
                temp = temp**(5) 

                self.elevation_map[y][x] = temp               
        print("Finished modifying elevation")

    def modify_temperature_map_with_cold_spots(self):
        for y in range(self.size[1]):   
            for x in range(self.size[0]):
                temp = self.temperature_map[y][x]
                custom = self.temperature_function(y, x, self.colds, self.size[0], self.scale)
                temp -= custom 
                temp = temp / (1.00 + 0.75 + 0.33 + 0.33 + 0.33+0.50)
                temp = temp**(5) 
                self.elevation_map[y][x] = temp
        print("Finished modifying elevation")

    def modify_elevation_map_with_lake(self, lake):
        for y in range(self.size[1]):   
            for x in range(self.size[0]):
                d = math.sqrt( (x-lake[0])**2+(y-lake[1])**2)
                if(d <= 10):
                    self.elevation_map[y][x] -= self.lake_function(x,y,lake,self.size[0])                
        print("Finished modifying lake")

    def create_countries(self, heights, n):
        countries = []
        new_country = ()
        new_country = new_country + (heights[0],)
        new_country = new_country + (heights[1],)
        countries.append(new_country)
        second_country = ()
        second_country = second_country + (heights[2],)
        countries.append(second_country)
        return countries

    def find_country_index_by_height(self, height, countries):
        idx = [item for item in countries if height in item]
        # print("++++++++++")
        # print(countries)
        # print(height)
        # print(idx[0])
        #country = countries.index(idx[0])
        country = idx[0]
        # print("++++++++++")
        return countries.index(country)

    def create_countries_map(self, heights, countries):       
        for y in range(self.size[1]):   
            for x in range(self.size[0]):
                country_index =  self.countries_function(y, x, heights, countries)
                self.countries_map[y][x] = country_index
        print("Finished creating countries map")

    def countries_function(self, x, y, heights, countries): # [(1,1),(2,2)(3,3)] [(1,2)]
        dist = 1000
        min = 0
        n=0
        for height in heights:
            height_x = height[0]
            height_y = height[1]
            tmp_dist = math.sqrt( (x-height_x)**2+(y-height_y)**2)
            if tmp_dist <= dist:
                dist = tmp_dist
                min = height
            n+=1    

        country_index = self.find_country_index_by_height(min, countries)
        return country_index       

    def islands_function(self, x, y, heights, w, scale):
        dist = 1000
        bckp = scale[-5]
        ###
        #w = 800
        ###
        n = len(heights)
        for height in heights:
            height_x = height[0]
            height_y = height[1]
            tmp_dist = math.sqrt( (x-height_x)**2+(y-height_y)**2)
            if tmp_dist <= dist:
                dist = tmp_dist  
        dist = bckp * dist  
        # if n > 5:
        #     dist = bckp * dist #3*dist # 0.55 0 - big 1 - small islands_size
        # else:
        #     dist = scale[n-1]*dist
        return dist*2/w

    def generate_islands(self, width, height, n):
        print("Generating "+str(n)+" islands")
        heights = []
        while n:
            add = True   
            # *3 for 1000x1000 maps       
            x = randrange(0+width/10,width-width/10) 
            y = randrange(0+height/10,height-height/10)
            # x = randrange(0+180,width-180) 
            # y = randrange(0+180,height-180)
            h = (x,y)
            heights.append(h)
            n-=1
        print("Finished generating islands")
        return heights
    
    def lake_function(self, x, y, lake, w):
        dist = 10        
        lake_x = lake[0]
        lake_y = lake[1]
        tmp_dist = math.sqrt( (x-lake_x)**2+(y-lake_y)**2)
        if tmp_dist <= dist:
            dist = tmp_dist           
        return dist

    def generate_rivers(self, size, water_level, sea_level_factor):
        water_level = water_level + sea_level_factor
        elevation_map = self.elevation_map
        rivers_number = randrange(5,15)
        i=0 
        starting_points = []
        tries = 0
        print("Generating "+str(rivers_number)+" rivers")  
        while i < rivers_number:
            x = randrange(10,size[0]-10)
            y = randrange(10,size[1]-10)
            if elevation_map[y][x] > water_level+1.5: #water_level+0.7               
                point= (y,x)
                starting_points.append(point)
                i+=1
        print("Rivers:")   
        print(starting_points)
        #starting_points = [(500, 327), (627, 592), (681, 567), (522, 263), (710, 226), (610, 372), (637, 579), (392, 251), (612, 401)]
        rivers = []
        extra_rivers = []
        for point in starting_points:                
            extra = randrange(5, 20) # 8 15
            river = self.generate_river(size, rivers, point, elevation_map, False, water_level)
            if river == None:
                continue
            # connection_points = [i for i in river if elevation_map[int(i[1])][int(i[0])] > water_level]           
            # # if extra > len(connection_points):
            # #      extra = len(connection_points)
            # # extra_points = sample(connection_points, extra) #connection_points[-extra:] #
            # extra_points = connection_points[-extra:]
            rivers.append(river)
            # for extra_point in extra_points:
            #     extra_river = self.generate_river(size, extra_rivers, extra_point, elevation_map, True, water_level)
            #     extra_rivers.append(extra_river)
        self.rivers = rivers
        #self.extra_rivers = extra_rivers
        print("Finished generating rivers")

    def generate_extra_rivers(self, size, water_level, sea_level_factor):
        water_level = water_level + sea_level_factor
        elevation_map = self.elevation_map         
#################################
# Generating rivers - to refactor
#################################
    def generate_river(self, size, rivers, starting_point, elevation_map, is_extra_river, water_level):
        angles = np.arange(0.0, 371.25, 11.25)
        angles2 = np.arange(0.0, 405, 55)
        line_len = 3
        river = [] 
        
        current_x = int(starting_point[0])
        current_y = int(starting_point[1])       
        current_height = elevation_map[current_x ][current_y] 
        p = (current_x, current_y)
        river.append(p)
        segments = 0
        while True:
            start_angle = 0
            steepness = 0
            tmp_x = 0
            tmp_y = 0
            tmp_height = 0
            tmp_list = []
            max_steepness = 0
            i = 0
            loop = True
            end = False
            outside = False
            while loop:
                for angle in angles:            
                    x = current_x + math.cos(angle)*(line_len+i*2)
                    y = current_y + math.sin(angle)*(line_len+i*2)
                    if x >= size[0] or y >= size[1] or x <= 0 or y <= 0:
                        return None                        
                        tmp_x = current_x       
                        loop = False                        
                        end = True
                        tmp_y = current_y
                        tmp_height = current_height
                        break
                    height = elevation_map[int(x)][int(y)]
                    if is_extra_river:
                        new_steepness = current_height - height
                    else:
                        new_steepness = height - current_height
                    tmp_list.append(new_steepness)
                    if new_steepness < steepness:
                        tmp_x = x
                        loop = False
                        tmp_y = y
                        tmp_height = height
                        steepness = new_steepness
                    
                i=i+1
            current_height = tmp_height       
            current_x = tmp_x
            current_y = tmp_y
            p = (current_x, current_y)
            if is_extra_river == True:
                if self.is_inside_river(rivers, p, 2) == True:
                    break
            #rivers fix  
            river.append(p)
            if len(river)>1:
                previous = river[-2]
                d = math.sqrt( ((p[0]-previous[0])**2)+((p[1]-previous[1])**2))
                if d > 30:
                    new = self.get_smaller_river_chunks(previous, p)
                    river.pop()
                    river.extend(new)
            segments +=1
            if (is_extra_river and segments >= 14):
                end = True  
            if end == True:
                break
            if current_height < water_level:
                # hlp.count_water_pixels(p, elevation_map)
                # if hlp.cnt >= 400:
                #     hlp.set_cnt()
                #     break
                # else:
                #     hlp.set_cnt()
                #     return None
                if self.is_big_enought(size, elevation_map, angles, p, water_level) == True:
                    break
                # else:
                #     self.red_rivers.append(river)
                #     return None
                    #self.modify_elevation_map_with_lake(p)

                    
            #if (current_height < water_level and is_big_enought(elevation_map, angles2, p)) or end == True:
            #    break
        return river 

    def make_rivers_deep(self, rivers, elevation_map, width):
        for river in rivers:
            i = 0
            for previous, current in zip(river, river[1:]):    
            #for point in river[1:]:
                # print("Pre points")
                # print("len="+str(len(river)))
                # print(i) 
                i+=1           
                p1 = int(previous[0])
                p2 = int(previous[1])
                p3 = int(current[0])
                p4 = int(current[1])
                # print(p1)
                # print(p2)
                # print(p3)
                # print(p4)

                points = hlp.plot_line(p1, p2, p3, p4, width)
                #print("Points done")
                for p in points:
                    elevation_map[p[0],p[1]] -= 3 #5 calkiem ok
                #print("Segment done")
            #print("=========River done===========") 

    def is_inside_river(self, rivers, point, radius):
        for river in rivers:
            for river_segment in river:
                d = math.sqrt( ((river_segment[0]-point[0])**2)+((river_segment[1]-point[1])**2))
                if d <= radius:
                    return True
        return False

    def is_big_enought(self, size, elevation_map, angles, p, water_level):
        px = p[1]
        py = p[0]
        count = 0
        for angle in angles:            
            x = px + math.cos(angle)*10 #20 
            y = py + math.sin(angle)*10 #20
            if x > size[0] or y > size[1] or x <0 or y<0:
                continue
            if elevation_map[int(y)][int(x)] < water_level:
                count +=1
            #self.red_rivers.append(((px,py),(y,x)))
        if count >=10:
            return True
        return False

    def get_smaller_river_chunks(self, start, end): # zamiast end mamy liste punktów
        lineLen = 5            
        maxAngle = math.radians(90)        
        minDistToEnd = 8 
        current = start
        new_points = []
        while True:
            xDist = end[0] - current[0]
            yDist = end[1] - current[1]
            between = math.atan2(yDist, xDist)   
            newAngle = between + (uniform(0,1) * maxAngle - maxAngle/2)
            x = current[0] + math.cos(newAngle) * lineLen
            y = current[1] + math.sin(newAngle) * lineLen
            point = (x,y)
            new_points.append(point)
            current = point
            distLeft = math.sqrt( ((end[0]-current[0])**2)+((end[1]-current[1])**2))

            if distLeft <= minDistToEnd:
                new_points.append(end)
                break
        return new_points

    def hydraulic_erosion(self, size, elevation_map, rivers):
        scale = 10
        eroded_map = elevation_map
        width = size[0]-1
        height = size[1]-1
        for y in range(1, height):
            for x in range(1, width): 
                done = False       
                for river in rivers:
                    if done == True:
                        break
                    for point in river:
                        river_x = point[0]
                        river_y = point[1]
                        tmp_dist = math.sqrt( (x-river_x)**2+(y-river_y)**2)
                        if tmp_dist <= 4: #4
                            eroded_map[y][x] -= (8-tmp_dist)/15
                            done = True
                            break               
        self.elevation_map = eroded_map
        print("Finished hydraulic erosion")
    
    def thermal_erosion(self, size, elevation_map):
        T = 0
        c = 0.1
        eroded_map = elevation_map
        width = size[0]-1
        height = size[1]-1
        for y in range(1, height):
            for x in range(1, width):
                y1 = y - 1
                y2 = y + 1
                x1 = x - 1
                x2 = x + 1   

                di = eroded_map[x][y] - eroded_map[x1][y1] 
                if di > T:         
                    eroded_map[x1][y1] += c*(di - T)
                    eroded_map[x][y] -= c*(di - T) 

                di = eroded_map[x][y] - eroded_map[x][y1] 
                if di > T:            
                    eroded_map[x][y1] += c*(di - T) 
                    eroded_map[x][y] -= c*(di - T) 

                di = eroded_map[x][y]-eroded_map[x2][y1] 
                if di > T:
                    eroded_map[x2][y1] += c*(di - T)
                    eroded_map[x][y] -= c*(di - T)  

                di = eroded_map[x][y]-eroded_map[x][y1] 
                if di > T:
                    eroded_map[x1][y] += c*(di - T) 
                    eroded_map[x][y] -= c*(di - T)

                di = eroded_map[x][y]-eroded_map[x2][y] 
                if di > T:
                    eroded_map[x2][y] += c*(di - T) 
                    eroded_map[x][y] -= c*(di - T)

                di = eroded_map[x][y]-eroded_map[x1][y2] 
                if di > T:
                    eroded_map[x1][y2] += c*(di - T)
                    eroded_map[x][y] -= c*(di - T)

                di = eroded_map[x][y]-eroded_map[x][y2] 
                if di > T:
                    eroded_map[x][y2] += c*(di - T)
                    eroded_map[x][y] -= c*(di - T)

                di = eroded_map[x][y]- eroded_map[x2][y2] 
                if di > T:
                    eroded_map[x2][y2] += c*(di - T)
                    eroded_map[x][y] -= c*(di - T)  
        return eroded_map