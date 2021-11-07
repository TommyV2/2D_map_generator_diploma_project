import numpy as np
from main import *
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d
from scipy.spatial import cKDTree
from PIL import Image, ImageDraw
import test2
import math

# rng = np.random.default_rng(seed=32)
# points = rng.random((1000,2))*799
##
world = None
country_regions_list = None

def calculate_country_borders(country_centers):
    global world
    global country_regions_list
    #test2.prepare()
    points = test2.points
    voronoi_kdtree = test2.voronoi_kdtree
    world = test2.world
    n = len(country_centers)
    z = len(points)
    print(n)
    print(z)
    country_points_list = []
    country_points_list = [[] for i in range(n)]
    country_regions_list = []
    country_regions_list = [[] for i in range(n)]
    country_colors_list = [(125,0,0), (161, 121, 63), (107, 171, 65)]

    country_index = 0
    for point in points:
        min = 1000
        for i, country_center in enumerate(country_centers):
            d = math.sqrt((point[1]-country_center[0])**2 + (point[0]-country_center[1])**2)
            if d < min:
                min = d
                country_index = i
        country_points_list[country_index].append((point[0],point[1]))
    v = len(country_points_list)
    print(v)
    for i,country_points in enumerate(country_points_list):  
        test_point_dist2, test_point_regions2 = voronoi_kdtree.query(country_points)
        country_regions_list[i] = test_point_regions2

    # img = Image.new( 'RGB', (800, 800), "black")
    # pixels = img.load()
    
    # for y in range(800):
    #     for x in range(800):
    #         region = int(world[y][x])
    #         pixel = (0,0,138)
    #         idx = [i for i,item in enumerate(country_regions_list) if region in item]        
    #         id = idx[0]
    #         pixel = country_colors_list[id]              
    #         pixels[x,y] = pixel
    # img.show()        
    # img = img.save("image.jpg", format='JPEG', subsampling=0, quality=100 )        

# regions
# ridge_vertices