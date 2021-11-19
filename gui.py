import pygame
import pygame_gui
import main
import numpy as np
from threading import Thread
import gui_helpers
from start_data_object import StartDataObject
from random import randrange, uniform
from helper import *
import prepare_voronoi
import random

MAX_CIVS = 4

def init_data_object(temperature_factor, elevation, mountains_factor, sea_level_factor, is_rivers, selected_heights, selected_scale, is_civilizations, civs, is_borders):
    size = (800, 800)
    elevation_seed_index = 1 #randrange(1,2)
    temperature_seed_index = 1 #randrange(1,10)
    elevation_seed =  elevation # np.loadtxt("elevation_seeds/seed"+str(elevation_seed_index)+".txt")
    temperature_seed = np.loadtxt("temperature_seeds/seed"+str(temperature_seed_index)+".txt")
    scale = selected_scale#get_random_scale()           
    is_rivers = is_rivers
    civilisations = is_civilizations
    water_level = 0.3
    temperature_factor = temperature_factor #-0.6 |snieg| -0.1 |trawa| 0.7 piach
    mountains_factor = mountains_factor
    sea_level_factor = sea_level_factor
    islands_number = randrange(1,10)
    heights = selected_heights
    borders = is_borders
    if heights == None or heights == []:
        for i in range(islands_number):
            x = randrange(0+width/10,width-width/10) 
            y = randrange(0+height/10,height-height/10)  
            h = (x,y)
            heights.append(h)

    civs = civs
    if civs == None or civs == []:
        n = random.randint(2,MAX_CIVS)
        n=2
        civs = heights[:n]

    elif len(civs) > MAX_CIVS:
        civs = civs[:MAX_CIVS]
    data_object = StartDataObject(size, elevation_seed, temperature_seed, scale, is_rivers, 
        civilisations, borders, water_level, temperature_factor, islands_number, mountains_factor, sea_level_factor, heights, civs) 
    return data_object

pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('lucidaconsole', 22)
myfont2 = pygame.font.SysFont('lucidaconsole', 22, bold=True)
##### GUI ELEMENTS #############################################################
pygame.display.set_caption('Map generator')
prepare_voronoi.prepare()
width = 1200
height = 870
window_surface = pygame.display.set_mode((width, height))
background = pygame.Surface((width, height))
background.fill(pygame.Color('#88888888'))
STARTLINE = 30
OFFSET = 60
ENDLINE = 850
display1 = pygame.Surface((820, 820))
display1.fill(pygame.Color('#2b2929'))
display2 = pygame.Surface((800, 800))
display2.fill(pygame.Color('#cdc8e0'))
hot_png = pygame.image.load("gui_visuals/hot.png")
cold_png = pygame.image.load("gui_visuals/cold.png")
high_png = pygame.image.load("gui_visuals/high.png")
low_png = pygame.image.load("gui_visuals/low.png")
high_water_png = pygame.image.load("gui_visuals/high_water.png")
low_water_png = pygame.image.load("gui_visuals/low_water.png")
height_png = pygame.image.load("gui_visuals/height.png")
islands_png = pygame.image.load("gui_visuals/islands.png")
moderate_png = pygame.image.load("gui_visuals/moderate.png")
land_png = pygame.image.load("gui_visuals/land.png")
hot_png.convert()
cold_png.convert()
high_png.convert()
low_png.convert()
high_water_png.convert()
low_water_png.convert()
height_png.convert()
islands_png.convert()
moderate_png.convert()
land_png.convert()

# TEMPERATURE
temperature_bar = pygame.Surface((gui_helpers.BAR_LENGTH, gui_helpers.BAR_WIDTH))
temperature_bar.fill(pygame.Color('#cdc8e0'))
temperature_pointer = pygame.Surface((20, gui_helpers.BAR_WIDTH))
temperature_pointer.fill(pygame.Color('#2b2929'))
temperature_text = myfont.render('Temperature', False, (0, 0, 0))
#############

# MOUNTAINS
mountains_bar = pygame.Surface((gui_helpers.BAR_LENGTH, gui_helpers.BAR_WIDTH))
mountains_bar.fill(pygame.Color('#cdc8e0'))
mountains_pointer = pygame.Surface((20, gui_helpers.BAR_WIDTH))
mountains_pointer.fill(pygame.Color('#2b2929'))
mountains_text = myfont.render('Mountains', False, (0, 0, 0))
#############

# SEA LEVEL
sea_level_bar = pygame.Surface((gui_helpers.BAR_LENGTH, gui_helpers.BAR_WIDTH))
sea_level_bar.fill(pygame.Color('#cdc8e0'))
sea_level_pointer = pygame.Surface((20, gui_helpers.BAR_WIDTH))
sea_level_pointer.fill(pygame.Color('#2b2929'))
sea_level_text = myfont.render('Sea Level', False, (0, 0, 0))
#############

bars = []
bars.append((gui_helpers.BARS_X, gui_helpers.TEMPERATURE_BAR_Y))
bars.append((gui_helpers.BARS_X, gui_helpers.TEMPERATURE_BAR_Y + OFFSET))
bars.append((gui_helpers.BARS_X, gui_helpers.TEMPERATURE_BAR_Y + 2*OFFSET))
scale_buttons = []
scale_buttons.append((gui_helpers.BARS_X, gui_helpers.SCALE_BUTTON_Y+10))
scale_buttons.append((gui_helpers.BARS_X+1.5*OFFSET, gui_helpers.SCALE_BUTTON_Y+10))
scale_buttons.append((gui_helpers.BARS_X+3*OFFSET, gui_helpers.SCALE_BUTTON_Y+10))

selected_scale_outline = pygame.Surface((84, 84))
selected_scale_outline.fill(pygame.Color('#ff0000'))

#manager = pygame_gui.UIManager((width, height))
manager = pygame_gui.UIManager((width, height), 'theme.json')
is_rivers = True
is_rivers_text = myfont.render('Rivers', False, (0, 0, 0))
is_rivers_text_2 = myfont2.render("Yes", False, (3, 63, 5))
is_civilizations = True
is_civilizations_text = myfont.render('Civilizations', False, (0, 0, 0))
is_civilizations_text_2 = myfont2.render("Yes", False, (3, 63, 5))
is_borders = True
is_borders_text = myfont.render('Borders', False, (0, 0, 0))
is_borders_text_2 = myfont2.render("Yes", False, (3, 63, 5))
scale_text = myfont.render('Land type', False, (0, 0, 0))
status_text = myfont.render("", False, (0, 0, 0))

is_rivers_button_yes = pygame_gui.elements.UIButton(object_id="button" ,relative_rect=pygame.Rect((gui_helpers.BARS_X, gui_helpers.IS_RIVERS_BUTTON_Y), (50, 50)),
                                            text='Yes',
                                            manager=manager)

is_rivers_button_no = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((gui_helpers.BARS_X + OFFSET, gui_helpers.IS_RIVERS_BUTTON_Y), (50, 50)),
                                            text='No',
                                            manager=manager) 

is_civilisations_button_yes = pygame_gui.elements.UIButton(object_id="button" ,relative_rect=pygame.Rect((gui_helpers.BARS_X, gui_helpers.IS_CIVILIZATIONS_BUTTON_Y), (50, 50)),
                                            text='Yes',
                                            manager=manager)

is_civilisations_button_no = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((gui_helpers.BARS_X + OFFSET, gui_helpers.IS_CIVILIZATIONS_BUTTON_Y), (50, 50)),
                                            text='No',
                                            manager=manager)
is_borders_button_yes = pygame_gui.elements.UIButton(object_id="button" ,relative_rect=pygame.Rect((gui_helpers.BARS_X, gui_helpers.IS_BORDERS_BUTTON_Y), (50, 50)),
                                            text='Yes',
                                            manager=manager)

is_borders_button_no = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((gui_helpers.BARS_X + OFFSET, gui_helpers.IS_BORDERS_BUTTON_Y), (50, 50)),
                                            text='No',
                                            manager=manager)                                

generate_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((width-200, ENDLINE-50), (100, 50)),
                                            text='Generate',
                                            manager=manager)
redraw_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((width-320, ENDLINE-50), (100, 50)),
                                            text='Redraw',
                                            manager=manager)

################################################################################

##### GENERATION PARAMETERS ####################################################
size = (800, 800)
elevation_seed_index = 1 #randrange(1,2)
temperature_seed_index = 1 #randrange(1,10)
elevation_seed = np.loadtxt("elevation_seeds/seed"+str(elevation_seed_index)+".txt")
temperature_seed = np.loadtxt("temperature_seeds/seed"+str(temperature_seed_index)+".txt")
scale = get_random_scale()           
is_rivers = True
civilisations = False
water_level = 0.3
temperature_factor = uniform(-0.6,0.8) #-0.6 |snieg| -0.1 |trawa| 0.7 piach
islands_number = randrange(1,10)
heights = None
civs = None
selected_heights = None
#################################################################################

clock = pygame.time.Clock()
is_running = True
finished = 0
img = None
temperature_factor = gui_helpers.selected_temperature
show_heights = False

while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False 
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == generate_button: 
                    elevation_seed = np.loadtxt("elevation_seeds/seed"+str(elevation_seed_index)+".txt")
                    start_data_object = init_data_object(temperature_factor, elevation_seed, mountains_factor, sea_level_factor, is_rivers, selected_heights, selected_scale, is_civilizations,civs, is_borders,  )
                    status_text = myfont.render("Loading...", False, (0, 0, 0))
                    thread = Thread(target = main.main, args=(start_data_object,))                  
                    thread.start()
                    show_heights = False
                    gui_helpers.selected_civs_initialized = True
                    #gui_helpers.selected_heights = []
                    # thread.join()
                if event.ui_element == redraw_button: 
                    status_text = myfont.render("Loading...", False, (0, 0, 0))            
                    thread = Thread(target = main.re_draw, args=(temperature_factor,mountains_factor, sea_level_factor, is_rivers, selected_heights,is_civilizations, is_borders, ))                  
                    thread.start()
                    show_heights = False                                         
                if event.ui_element == is_rivers_button_yes:
                    is_rivers_text_2 = myfont2.render("Yes", False, (3, 63, 5))
                    is_rivers = True
                if event.ui_element == is_rivers_button_no:
                    is_rivers = False 
                    is_rivers_text_2 = myfont2.render("No", False, (159, 35, 16)) 
                if event.ui_element == is_civilisations_button_yes:
                    is_civilizations_text_2 = myfont2.render("Yes", False, (3, 63, 5))
                    is_civilizations = True
                if event.ui_element == is_civilisations_button_no:
                    is_civilizations = False 
                    is_civilizations_text_2 = myfont2.render("No", False, (159, 35, 16))
                if event.ui_element == is_borders_button_yes:
                    is_borders_text_2 = myfont2.render("Yes", False, (3, 63, 5))
                    is_borders = True
                if event.ui_element ==is_borders_button_no:
                    is_borders = False 
                    is_borders_text_2 = myfont2.render("No", False, (159, 35, 16))                         
        if event.type == pygame.MOUSEBUTTONUP:  
            gui_helpers.handle_bar_clicked(bars, event.pos)
            gui_helpers.handle_map_clicked((30, 40), event.pos)
            gui_helpers.handle_scale_clicked(scale_buttons, event.pos)
            civs = gui_helpers.selected_civs
            selected_heights = main.heights + gui_helpers.selected_heights
            
            temperature_factor = gui_helpers.selected_temperature
            mountains_factor = gui_helpers.selected_mountains
            sea_level_factor = gui_helpers.selected_sea_level
            selected_scale = gui_helpers.selected_scale
            show_heights = True

        manager.process_events(event)

    manager.update(time_delta)
    window_surface.blit(background, (0, 0))
    window_surface.blit(display1, (20, 30))
    window_surface.blit(display2, (30, 40))

    window_surface.blit(cold_png, (gui_helpers.BARS_X-30, gui_helpers.TEMPERATURE_BAR_Y))
    window_surface.blit(hot_png, (gui_helpers.BARS_X+gui_helpers.BAR_LENGTH+10, gui_helpers.TEMPERATURE_BAR_Y))  
    window_surface.blit(temperature_bar, (gui_helpers.BARS_X, gui_helpers.TEMPERATURE_BAR_Y))
    window_surface.blit(temperature_pointer, (gui_helpers.temperature_pointer_x-10, gui_helpers.TEMPERATURE_BAR_Y))
    window_surface.blit(temperature_text,(gui_helpers.BARS_X, gui_helpers.TEMPERATURE_BAR_Y-30))

    window_surface.blit(low_png, (gui_helpers.BARS_X-30, gui_helpers.MOUNTAINS_BAR_Y))
    window_surface.blit(high_png, (gui_helpers.BARS_X+gui_helpers.BAR_LENGTH+10, gui_helpers.MOUNTAINS_BAR_Y)) 
    window_surface.blit(mountains_bar, (gui_helpers.BARS_X, gui_helpers.MOUNTAINS_BAR_Y))
    window_surface.blit(mountains_pointer, (gui_helpers.mountains_pointer_x-10, gui_helpers.MOUNTAINS_BAR_Y))
    window_surface.blit(mountains_text,(gui_helpers.BARS_X, gui_helpers.MOUNTAINS_BAR_Y-30))

    window_surface.blit(low_water_png, (gui_helpers.BARS_X-30, gui_helpers.SEA_LEVEL_BAR_Y))
    window_surface.blit(high_water_png, (gui_helpers.BARS_X+gui_helpers.BAR_LENGTH+10, gui_helpers.SEA_LEVEL_BAR_Y)) 
    window_surface.blit(sea_level_bar, (gui_helpers.BARS_X, gui_helpers.SEA_LEVEL_BAR_Y))
    window_surface.blit(sea_level_pointer, (gui_helpers.sea_level_pointer_x-10, gui_helpers.SEA_LEVEL_BAR_Y))
    window_surface.blit(sea_level_text,(gui_helpers.BARS_X, gui_helpers.SEA_LEVEL_BAR_Y-30))

    window_surface.blit(is_rivers_text,(gui_helpers.BARS_X, gui_helpers.IS_RIVERS_BUTTON_Y-30))
    window_surface.blit(is_rivers_text_2,(gui_helpers.BARS_X + 2*OFFSET+20, gui_helpers.IS_RIVERS_BUTTON_Y+15))

    window_surface.blit(is_civilizations_text,(gui_helpers.BARS_X, gui_helpers.IS_CIVILIZATIONS_BUTTON_Y-30))
    window_surface.blit(is_civilizations_text_2,(gui_helpers.BARS_X + 2*OFFSET+20, gui_helpers.IS_CIVILIZATIONS_BUTTON_Y+15))
    
    window_surface.blit(is_borders_text,(gui_helpers.BARS_X, gui_helpers.IS_BORDERS_BUTTON_Y-30))
    window_surface.blit(is_borders_text_2,(gui_helpers.BARS_X + 2*OFFSET+20, gui_helpers.IS_BORDERS_BUTTON_Y+15))

    window_surface.blit(scale_text,(gui_helpers.BARS_X, gui_helpers.SCALE_BUTTON_Y-30))
    window_surface.blit(selected_scale_outline,(gui_helpers.scale_outline[0]-2, gui_helpers.scale_outline[1]+8))
    window_surface.blit(islands_png,(gui_helpers.BARS_X, gui_helpers.SCALE_BUTTON_Y+10))
    window_surface.blit(moderate_png,(gui_helpers.BARS_X+1.5*OFFSET, gui_helpers.SCALE_BUTTON_Y+10))
    window_surface.blit(land_png,(gui_helpers.BARS_X+3*OFFSET, gui_helpers.SCALE_BUTTON_Y+10))

    manager.draw_ui(window_surface)
    finished = main.finished
    if finished:
        try:
            img = pygame.image.load("image.jpg")
            img.convert()
            finished = 0
            status_text = myfont.render("Finished", False, (0, 0, 0))
        except:
            print("Failed to load img")

    if img != None:
        window_surface.blit(img, (30, 40))  
    if show_heights:
        for selected_height in selected_heights:
            window_surface.blit(height_png, (selected_height[1], selected_height[0]))
    window_surface.blit(status_text, (400, 6)) 
    pygame.display.update()


