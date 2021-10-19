from opensimplex import OpenSimplex
import numpy as np
import time

def noise(nx, ny):
    # Rescale from -1.0:+1.0 to 0.0:1.0
    return gen.noise2d(nx, ny) / 2.0 + 0.5

size = 1200
start = time.time()
for seed in range(1,2):
    map = []
    filename = 'elevation_seeds_1000/seed'+str(seed)+'.txt'
    gen = OpenSimplex(seed)
    for y in range(size):
        map.append([0] * size)
        for x in range(size):       
            nx=x/size - 0.5
            ny=y/size - 0.5
            e = (0.54 * noise( 4 * nx,  4 * ny)
                + 0.50 * noise( 8 * nx,  8 * ny)
                + 0.25 * noise( 16 * nx,  16 * ny)
                + 0.13 * noise( 64 * nx,  64 * ny))
            e = 1+e #-custom       
            #e = e / (0.54 + 0.50 + 0.25+ 0.13) #+ 0.06+ 0.03+0.015   
            #e = (e*1)**(5) # fudge, elevation_level
            map[y][x] = e
        
    numpy_map = np.array(map)
    np.savetxt(filename, numpy_map)
    now = time.time()
    print("Time: ", now-start)
    #print(seed)
    #with open(filename, 'w') as filehandle:
    #    for row in map:
    #        filehandle.write('%s\n' % row)
for seed in range(1,2):
    map = []
    filename = 'temperature_seeds_1000/seed'+str(seed)+'.txt'
    gen = OpenSimplex(seed)
    for y in range(size):
        map.append([0] * size)
        for x in range(size):       
            nx=x/size - 0.5
            ny=y/size - 0.5
            m = (1.00 * noise( 1 * nx,  1 * ny)
                + 0.75 * noise( 2 * nx,  2 * ny)
                + 0.33 * noise( 4 * nx,  4 * ny)
                 + 0.33 * noise( 8 * nx,  8 * ny)
                 + 0.33 * noise(16 * nx, 16 * ny)
                 + 0.50 * noise(32 * nx, 32 * ny))                         
            m = (m) / (1.00 + 0.75 + 0.33+ 0.33 + 0.33+ 0.50) # + 0.33+0.50) #+ 0.06+ 0.03+0.015               
            map[y][x] = m
        
    numpy_map = np.array(map)
    np.savetxt(filename, numpy_map)
    now = time.time()
    print("Time: ", now-start)
    print(seed)
end = time.time()
print("Time: ", end-start)
# y = np.loadtxt("elevation_seeds/seed1.txt")


    