from PIL import Image, ImageDraw

#Biomes:
WATER = (24, 161, 219)
ICE = (154, 245, 234)
BEACH = (185, 196, 100)
BEACH_COLD = (215, 215, 193)
BEACH_HOT = (254, 210, 107)
DESERT = (161, 121, 63)
GRASS = (107, 171, 65)
ROCKS = (176, 164, 146)
FOREST = (8, 84, 26)
COLD_FOREST = (52, 99, 96)
JUNGLE = (8, 84, 23)
SNOW = (237, 236, 230)
#mountains
# DESERT_MOUNTAINS_6 = (31, 22, 22)
# DESERT_MOUNTAINS_5 = (38, 28, 28)
# DESERT_MOUNTAINS_4 = (51, 38, 38)
# DESERT_MOUNTAINS_3 = (63, 39, 1)
# DESERT_MOUNTAINS_2 = (97, 62, 2)
# DESERT_MOUNTAINS_1 = (145, 96, 12)

#1
# MOUNTAINS_7 = (24, 24, 24)
# MOUNTAINS_6 = (32, 32, 32)
# MOUNTAINS_5_6 = (40, 40, 40)
# MOUNTAINS_5 = (48, 48, 48)
# MOUNTAINS_4_5 = (59, 59, 59)
# MOUNTAINS_4 = (70, 70, 70)
# MOUNTAINS_3_4 = (76, 76, 76)
# MOUNTAINS_3 = (82, 82, 82)
# MOUNTAINS_2_3 = (95, 95, 95)
# MOUNTAINS_2 = (9, 45, 19)
# MOUNTAINS_1 = (12, 63, 27)

#2
# MOUNTAINS_7 = (108, 108, 108)
# MOUNTAINS_6 = (95, 95, 95)
# MOUNTAINS_5_6 = (90, 90, 90)
# MOUNTAINS_5 = (85, 85, 85)
# MOUNTAINS_4_5 = (80, 80, 80)
# MOUNTAINS_4 = (75, 75, 75)
# MOUNTAINS_3_4 = (70, 70, 70)
# MOUNTAINS_3 = (65, 65, 65)
# MOUNTAINS_2_3 = (59, 59, 59)
# MOUNTAINS_2 = (59, 59, 59)
# MOUNTAINS_1 = (9, 45, 19)

#3
# MOUNTAINS_12 = (232, 232, 232)
# MOUNTAINS_11 = (210, 210, 210)
# MOUNTAINS_10 = (190, 190, 190)
# MOUNTAINS_9 = (170, 170, 170)
# MOUNTAINS_8 = (150, 150, 150)
# MOUNTAINS_7 = (130, 130, 130)
# MOUNTAINS_6 = (108, 108, 108)
# MOUNTAINS_5_6 = (95, 95, 95)
# MOUNTAINS_5 = (82, 82, 82)
# MOUNTAINS_4_5 = (76, 76, 76)
# MOUNTAINS_4 = (70, 70, 70)
# MOUNTAINS_3_4 = (59, 59, 59)
# MOUNTAINS_3 = (48, 48, 48)
# MOUNTAINS_2_3 = (40, 40, 40)
# MOUNTAINS_2 = (9, 45, 19)#(32, 32, 32)
# MOUNTAINS_1 = (12, 63, 27)

#4
# MOUNTAINS_12 = 
# MOUNTAINS_11 = 
# MOUNTAINS_10 = 
# MOUNTAINS_9 = (232, 232, 232)
# MOUNTAINS_8 = (210, 210, 210)
# MOUNTAINS_7 = (190, 190, 190)
# MOUNTAINS_6 = (170, 170, 170)
# MOUNTAINS_5_6 = (150, 150, 150)
# MOUNTAINS_5 = (130, 130, 130)
# MOUNTAINS_4_5 = (108, 108, 108)
# MOUNTAINS_4 = (95, 95, 95)
# MOUNTAINS_3_4 = (82, 82, 82)
# MOUNTAINS_3 = (76, 76, 76)
# MOUNTAINS_2_3 = (70, 70, 70)
# MOUNTAINS_2 =  (59, 59, 59)
# MOUNTAINS_1 = (9, 45, 19)

#5
# MOUNTAINS_7 = (108, 108, 108)
# MOUNTAINS_6 = (95, 95, 95)
# MOUNTAINS_5 = (85, 85, 85)
# MOUNTAINS_4 = (75, 75, 75)
# MOUNTAINS_3 = (65, 65, 65)
# MOUNTAINS_2 = (59, 59, 59)
# MOUNTAINS_1 = (9, 45, 19)

#6
# MOUNTAINS_11 = (150, 150, 150)
# MOUNTAINS_10 = (130, 130, 130)
# MOUNTAINS_9 = (110, 110, 110)
MOUNTAINS_8 = (150, 150, 150)
MOUNTAINS_7 = (130, 130, 130)
MOUNTAINS_6 = (110, 110, 110)
MOUNTAINS_5 = (90, 90, 90)
MOUNTAINS_4 = (70, 70, 70)
MOUNTAINS_3 = (50, 50, 50)
MOUNTAINS_2 = (9, 45, 19)
MOUNTAINS_1 = (12, 63, 27)
MOUNTAINS_OUTLINE = (37, 37, 37)

#1
# DESERT_MOUNTAINS_8 = (162, 152, 140)
# DESERT_MOUNTAINS_7 = (142, 132, 120)
# DESERT_MOUNTAINS_6 = (122, 112, 100)
# DESERT_MOUNTAINS_5 = (102, 92, 80)
# DESERT_MOUNTAINS_4 = (82, 72, 60)
# DESERT_MOUNTAINS_3 = (62, 52, 40)
# DESERT_MOUNTAINS_2 = (97, 63, 2)
# DESERT_MOUNTAINS_1 = (144, 96, 12)

#2
DESERT_MOUNTAINS_8 = (163, 139, 1)
DESERT_MOUNTAINS_7 = (143, 119, 1)
DESERT_MOUNTAINS_6 = (123, 99, 1)
DESERT_MOUNTAINS_5 = (103, 79, 1)
DESERT_MOUNTAINS_4 = (83, 59, 1)
DESERT_MOUNTAINS_3 = (78, 49, 1)# #(63, 39, 1)
DESERT_MOUNTAINS_2 = (144, 96, 12) #(97, 63, 2)
DESERT_MOUNTAINS_1 = (144, 96, 12)
DESERT_MOUNTAINS_OUTLINE = (52, 33, 1)

#3
# DESERT_MOUNTAINS_8 = (162, 152, 140)
# DESERT_MOUNTAINS_7 = (142, 132, 120)
# DESERT_MOUNTAINS_6 = (122, 112, 100)
# DESERT_MOUNTAINS_5 = (102, 92, 80)
# DESERT_MOUNTAINS_4 = (82, 72, 60)
# DESERT_MOUNTAINS_3 = (62, 52, 40)
# DESERT_MOUNTAINS_2 = (144, 96, 12) #(97, 63, 2)
# DESERT_MOUNTAINS_1 = (144, 96, 12)

COLD_MOUNTAINS_8 = (255, 255, 255)
COLD_MOUNTAINS_7 = (205, 205, 205)
COLD_MOUNTAINS_6 = (190, 190, 190)
COLD_MOUNTAINS_5 = (175, 175, 175)
COLD_MOUNTAINS_4 = (160, 160, 160)
COLD_MOUNTAINS_3 = (145, 145, 145)
COLD_MOUNTAINS_2 = (232, 232, 232)
COLD_MOUNTAINS_1 = (232, 232, 232)
COLD_MOUNTAINS_OUTLINE = (90, 90, 90)

# CIVILIZATIONS
RED_1 = (255,138,138)
RED_2 = (255,94,94)
RED_3 = (255,60,60)
RED_4 = (242,0,0)
RED_5 = (125,0,0)
RED_6 = (70,0,0)
RED_7 = (40,0,0)
RED_8 = (23,0,0)

BLUE_1 = (170,170,255)
BLUE_2 = (111,111,255)
BLUE_3 = (74,74,255)
BLUE_4 = (13,13,255)
BLUE_5 = (0,0,138)
BLUE_6 = (0,0,94)
BLUE_7 = (0,0,55)
BLUE_8 = (0,0,26)

GREEN_1 = (202,255,206)
GREEN_2 = (133,254,142)
GREEN_3 = (101,255,113)
GREEN_4 = (14,255,32)
GREEN_5 = (1,120,10)
GREEN_6 = (1,78,6)
GREEN_7 = (0,47,3)
GREEN_8 = (0,28,2)

PINK_1 = (254,184,252)
PINK_2 = (254,139,251)
PINK_3 = (254,107,251)
PINK_4 = (254,14,248)
PINK_5 = (131,1,128)
PINK_6 = (101,1,99)
PINK_7 = (73,1,71)
PINK_8 = (52,1,51)

country_colors = [(255, 0, 0), (0, 0, 204), (153, 0, 204), (70, 70, 70)]

#city_colors = [(23,0,0), (0,0,26), (52,1,51), (0,28,2)]

blue_capital = Image.open("gui_visuals/blue_capital.png", 'r')
blue_normal = Image.open("gui_visuals/blue_normal.png", 'r')

red_capital = Image.open("gui_visuals/red_capital.png", 'r')
red_normal = Image.open("gui_visuals/red_normal.png", 'r')

pink_capital = Image.open("gui_visuals/pink_capital.png", 'r')
pink_normal = Image.open("gui_visuals/pink_normal.png", 'r')

green_capital = Image.open("gui_visuals/green_capital.png", 'r')
green_normal = Image.open("gui_visuals/green_normal.png", 'r')

city_colors = [(red_capital, red_normal), (blue_capital, blue_normal),(pink_capital, pink_normal),(green_capital, green_normal)]
neutral_city = Image.open("gui_visuals/neutral_city.png", 'r')