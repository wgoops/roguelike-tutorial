import numpy as np 
from tcod.console import Console

import tile_types 

class GameMap: 
    def __init__(self, width:int, height:int):
        self.width, self.height = width, height
        self.tiles = np.full(
            (width, height), 
            fill_value = tile_types.wall, 
            order="F")

        self.visible = np.full((width, height), fill_value=False, order="F") #tiles player can currently see 
        self.explored = np.full((width, height), fill_value=False, order="F") #tiles player's explored previously


    def in_bounds(self, x:int, y:int) -> bool: 
        """Return True if x and y are inside of the bounds of this map."""
        return 0 <= x < self.width and 0 <= y < self.height

    def render(self, console: Console) -> None:
        """
        Renders the map. 

        There are two arrays: visible, and explored.

        When a tile is visible, we want to color it with "light" colors.
        When a tile isn't visible, but we've explored it, we want to color it with "dark" colors.
        When a tile just hasn't been explored at all, we'll default to SHROUD. 
        """

        console.tiles_rgb[0:self.width, 0:self.height] = np.select(
            condlist = [self.visible, self.explored],
            choicelist = [self.tiles["light"], self.tiles["dark"]],
            default = tile_types.SHROUD
        )
