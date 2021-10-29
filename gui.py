import pygame
import pygame_gui
import main
import numpy as np
from threading import Thread
import gui_helpers
from start_data_object import StartDataObject
from random import randrange, uniform
from helper import *

def init_data_object(temperature_factor, elevation, mountains_factor, sea_level_factor, is_rivers):
    size = (800, 800)
    elevation_seed_index = 1 #randrange(1,2)
    temperature_seed_index = 1 #randrange(1,10)
    elevation_seed =  elevation # np.loadtxt("elevation_seeds/seed"+str(elevation_seed_index)+".txt")
    temperature_seed = np.loadtxt("temperature_seeds/seed"+str(temperature_seed_index)+".txt")
    scale = get_random_scale()           
    is_rivers = is_rivers
    civilisations = False
    water_level = 0.3
    temperature_factor = temperature_factor #-0.6 |snieg| -0.1 |trawa| 0.7 piach
    mountains_factor = mountains_factor
    sea_level_factor = sea_level_factor
    islands_number = randrange(1,10)
    heights = None
    data_object = StartDataObject(size, elevation_seed, temperature_seed, scale, is_rivers, 
        civilisations, water_level, temperature_factor, islands_number, mountains_factor, sea_level_factor, heights) 
    return data_object

pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('lucidaconsole', 22)
##### GUI ELEMENTS #############################################################
pygame.display.set_caption('Map generator')

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



manager = pygame_gui.UIManager((width, height))

is_rivers = True
is_rivers_text = myfont.render('Rivers', False, (0, 0, 0))
is_rivers_button_yes = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((gui_helpers.BARS_X, gui_helpers.IS_RIVERS_BUTTON_Y), (50, 50)),
                                            text='Yes',
                                            manager=manager)

is_rivers_button_no = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((gui_helpers.BARS_X + OFFSET, gui_helpers.IS_RIVERS_BUTTON_Y), (50, 50)),
                                            text='No',
                                            manager=manager)                               

generate_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((width-200, ENDLINE-50), (100, 50)),
                                            text='Generate',
                                            manager=manager)
redraw_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((width-200, ENDLINE-150), (100, 50)),
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
#################################################################################

clock = pygame.time.Clock()
is_running = True
finished = 0
img = None
temperature_factor = gui_helpers.selected_temperature


while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False 
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == generate_button: 
                    elevation_seed = np.loadtxt("elevation_seeds/seed"+str(elevation_seed_index)+".txt")
                    start_data_object = init_data_object(temperature_factor, elevation_seed, mountains_factor, sea_level_factor, is_rivers)
                    thread = Thread(target = main.main, args=(start_data_object,))                  
                    thread.start()
                    # thread.join()
                if event.ui_element == redraw_button:
                    thread = Thread(target = main.re_draw, args=(temperature_factor,mountains_factor, sea_level_factor, is_rivers,))                  
                    thread.start() 
                if event.ui_element == is_rivers_button_yes:
                    is_rivers = True
                if event.ui_element == is_rivers_button_no:
                    is_rivers = False                       
        if event.type == pygame.MOUSEBUTTONUP:  
            gui_helpers.handle_bar_clicked(bars, event.pos)
            temperature_factor = gui_helpers.selected_temperature
            mountains_factor = gui_helpers.selected_mountains
            sea_level_factor = gui_helpers.selected_sea_level
        manager.process_events(event)

    manager.update(time_delta)
    window_surface.blit(background, (0, 0))
    window_surface.blit(display1, (20, 30))
    window_surface.blit(display2, (30, 40))

    window_surface.blit(is_rivers_text,(gui_helpers.BARS_X, gui_helpers.IS_RIVERS_BUTTON_Y-30))

    window_surface.blit(temperature_bar, (gui_helpers.BARS_X, gui_helpers.TEMPERATURE_BAR_Y))
    window_surface.blit(temperature_pointer, (gui_helpers.temperature_pointer_x-10, gui_helpers.TEMPERATURE_BAR_Y))
    window_surface.blit(temperature_text,(gui_helpers.BARS_X, gui_helpers.TEMPERATURE_BAR_Y-30))

    window_surface.blit(mountains_bar, (gui_helpers.BARS_X, gui_helpers.MOUNTAINS_BAR_Y))
    window_surface.blit(mountains_pointer, (gui_helpers.mountains_pointer_x-10, gui_helpers.MOUNTAINS_BAR_Y))
    window_surface.blit(mountains_text,(gui_helpers.BARS_X, gui_helpers.MOUNTAINS_BAR_Y-30))

    window_surface.blit(sea_level_bar, (gui_helpers.BARS_X, gui_helpers.SEA_LEVEL_BAR_Y))
    window_surface.blit(sea_level_pointer, (gui_helpers.sea_level_pointer_x-10, gui_helpers.SEA_LEVEL_BAR_Y))
    window_surface.blit(sea_level_text,(gui_helpers.BARS_X, gui_helpers.SEA_LEVEL_BAR_Y-30))

    manager.draw_ui(window_surface)
    finished = main.finished
    if finished:
        img = pygame.image.load("image.jpg")
        img.convert()
        finished = 0

    if img != None:
        window_surface.blit(img, (30, 40))  


    pygame.display.update()


