
BAR_LENGTH = 200
BAR_WIDTH = 20

BARS_X = 900
OFFSET = 60

TEMPERATURE_BAR_Y = 100
MOUNTAINS_BAR_Y = TEMPERATURE_BAR_Y + OFFSET
SEA_LEVEL_BAR_Y = TEMPERATURE_BAR_Y + 2*OFFSET
IS_RIVERS_BUTTON_Y = TEMPERATURE_BAR_Y + 3*OFFSET
IS_CIVILIZATIONS_BUTTON_Y = TEMPERATURE_BAR_Y + 4.5*OFFSET

temperature_pointer_x = BARS_X + BAR_LENGTH/2
selected_temperature = 0.1

mountains_pointer_x = BARS_X + BAR_LENGTH/2
selected_mountains = 0

sea_level_pointer_x = BARS_X + BAR_LENGTH/2
selected_sea_level = 0

selected_heights = []

def handle_bar_clicked(bars, position):
    for bar in bars:
        if is_inside_rect((bar[0], bar[1]+BAR_WIDTH), (bar[0]+BAR_LENGTH, bar[1]), position):
            if bar[1] == TEMPERATURE_BAR_Y:
                handle_temperature_bar(position)
                break
            elif bar[1] == MOUNTAINS_BAR_Y:
                handle_mountains_bar(position)
                break
            elif bar[1] == SEA_LEVEL_BAR_Y:
                handle_sea_level_bar(position)
                break
def handle_map_clicked(map, position):
    bottom_left = (map[0],map[1]+800)
    top_right = (map[0]+800,map[1])
    if is_inside_rect(bottom_left, top_right, position):
        selected_heights.append((position[1], position[0]))

def is_inside_rect(bottom_left, top_right, point):
    if (point[0] > bottom_left[0] and point[0] < top_right[0] and point[1] < bottom_left[1] and point[1] > top_right[1]):
        return True
    else:
        return False

def handle_temperature_bar(position):
    start = BARS_X
    level = position[0]
    temperature_spectrum = (-0.6, 0.8)
    range = temperature_spectrum[1] - temperature_spectrum[0]
    percent = (level - start) / BAR_LENGTH
    global temperature_pointer_x
    global selected_temperature
    selected_temperature = temperature_spectrum[0] + percent * range
    temperature_pointer_x = BARS_X + percent * BAR_LENGTH

def handle_mountains_bar(position):
    start = BARS_X
    level = position[0]
    mountains_spectrum = (-0.8, 0.8)
    range = mountains_spectrum[1] - mountains_spectrum[0]
    percent = (level - start) / BAR_LENGTH
    global mountains_pointer_x
    global selected_mountains
    selected_mountains = mountains_spectrum[0] + percent * range
    mountains_pointer_x = BARS_X + percent * BAR_LENGTH
    print(selected_mountains)
    print(mountains_pointer_x)

def handle_sea_level_bar(position):
    start = BARS_X
    level = position[0]
    sea_level_spectrum = (-0.25, 0.25)
    range = sea_level_spectrum[1] - sea_level_spectrum[0]
    percent = (level - start) / BAR_LENGTH
    global sea_level_pointer_x
    global selected_sea_level
    selected_sea_level = sea_level_spectrum[0] + percent * range
    sea_level_pointer_x = BARS_X + percent * BAR_LENGTH
    print(selected_sea_level)
    print(sea_level_pointer_x)


