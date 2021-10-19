import math
from random import randrange, uniform

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
