import numpy as np
from main import *
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d
from scipy.spatial import cKDTree
from PIL import Image, ImageDraw
import test2
import math

world = None
country_regions_list = None

def calculate_country_borders(country_centers):
    global world
    global country_regions_list
    points = test2.points
    voronoi_kdtree = test2.voronoi_kdtree
    world = test2.world
    n = len(country_centers)
    z = len(points)
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
    for i,country_points in enumerate(country_points_list):  
        test_point_dist2, test_point_regions2 = voronoi_kdtree.query(country_points)
        country_regions_list[i] = test_point_regions2