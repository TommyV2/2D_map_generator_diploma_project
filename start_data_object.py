from dataclasses import dataclass
import numpy as np
from numpy.core.records import array

@dataclass
class StartDataObject:
    size: tuple
    elevation_seed: np.ndarray
    temperature_seed: np.ndarray
    scale: tuple
    is_rivers: bool
    civilisations: bool
    borders: bool
    water_level: float
    temperature_factor: float
    islands_number: int
    mountains_factor: float
    sea_level_factor: float
    urbanization_level_factor: float
    heights: list = None
    civs: list = None
    