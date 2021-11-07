import numpy as np
from main import *
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d
from scipy.spatial import cKDTree
from PIL import Image, ImageDraw

points = None
all_regions = None
voronoi_kdtree = None
world = None

def prepare():
    global points
    global all_regions
    global voronoi_kdtree
    global world

    rng = np.random.default_rng(seed=32)
    points = rng.random((2000,2))*799

    vor = Voronoi(points)
    all_regions = vor.point_region
    voronoi_kdtree = cKDTree(points)

    list = []
    for y in range(800):
        for x in range(800):
            p = (x,y)
            list.append(p)
    extraPoints = list
    test_point_dist, test_point_regions = voronoi_kdtree.query(extraPoints)
    result = np.reshape(test_point_regions, (-1, 800))

    world = np.zeros((800,800))
    for y in range(800):
        for x in range(800):
            world[y][x] = result[y][x]