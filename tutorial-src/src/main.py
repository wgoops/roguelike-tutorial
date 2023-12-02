#!/usr/bin/env python3
import tcod 
from engine import Engine
import entity_factories
import copy
from procgen import generate_dungeon

def main(): 

    ##set screen settings 
    screen_width = 120
    screen_height = 75

    map_width = 80
    map_height = 45

    room_max_size = 10
    room_min_size = 6
    max_rooms = 6
    max_monsters_per_room = 3
    ##import tileset
    
    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )   #TODO make path to png not absolutely awful

    ## set up event handler
    player = copy.deepcopy(entity_factories.player)
    engine = Engine(player=player)

    ## create dungeon
    engine.game_map = generate_dungeon(
        map_width=map_width,
        map_height=map_height, 
        max_rooms=max_rooms,
        room_min_size=room_min_size,
        room_max_size=room_max_size,
        engine=engine,
        max_monsters_per_room=max_monsters_per_room,
    )

    engine.update_fov()

    ## define screen settings
    terminal = tcod.context.new_terminal(
        columns = screen_width,
        rows = screen_height,
        tileset = tileset,
        title = "Yet Another Roguelike Tutorial",
        vsync = True,
        #sdl_window_flags=tcod.context.SDL_WINDOW_FULLSCREEN_DESKTOP
    )
        
    ## create screen
    with terminal as context: 
        root_console = tcod.console.Console(screen_width, screen_height, order="F")
        
        ## SET UP GAME LOOP, VERY IMPORTANT
        while True: 

            # DRAW CURRENT FRAME 
            engine.render(
                root_console, 
                context
            )
            engine.event_handler.handle_events()

if __name__ == "__main__":
    main()
    