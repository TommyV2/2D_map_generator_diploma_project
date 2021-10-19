import numpy as np


for i in range(1,11):
    elevation_seed = np.loadtxt("elevation_seeds/seed"+str(i)+".txt")
    mean = np.mean(elevation_seed, axis=0)
    minimal = np.min(elevation_seed)
    maximal = np.max(elevation_seed)
    print(f"Seed{i} min={minimal} max={maximal} avg={minimal}")