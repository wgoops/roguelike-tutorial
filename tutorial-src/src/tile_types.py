from typing import Tuple

import numpy as np

# "tiled graphics structured type compatible with Console.tiles.rbg" -- mystery stuff 

graphic_dt = np.dtype( #creates data type usable by numpy
    [
        ("ch", np.int32), #ch is character
        ("fg", "3B"), #fg is foreground color
        ("bg", "3B"), # bg is the background color
    ]
)

# "tiled struct used for statically defined tile data" -- mystery stuff TODO understand what is going on with tile_dt

tile_dt = np.dtype(
    [
        ("walkable", bool), # if this tile can be walked over, this is true
        ("transparent", bool), # if this tile doesn't block our field of view, this is true
        ("dark", graphic_dt), # when the tile is not in our field of view, these graphics are used
    ]
)

def new_tile(
    *, # Enforce the use of keywords, so that we don't have to worry about the order.
    walkable: int, 
    transparent: int,
    dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
) -> np.ndarray: 

    """ Helper function for defining individual tile types """ 
    return np.array((walkable, transparent, dark), dtype = tile_dt)


## TILE TYPES

floor = new_tile(
    walkable = True, 
    transparent = True, 
    dark = (ord(" "), (255,255,255), (50,50,150)), 
)

wall = new_tile(
    walkable = False, transparent = False, dark = (ord(" "), (255,255,255), (0,0,100))
)