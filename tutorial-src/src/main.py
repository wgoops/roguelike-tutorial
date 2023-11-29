#!/usr/bin/env python3
import tcod 
from engine import Engine
import entity_factories
import copy
from procgen import generate_dungeon
from input_handlers import EventHandler

def main(): 

    ##set screen settings 
    screen_width = 80
    screen_height = 50

    map_width = 80
    map_height = 45

    room_max_size = 10
    room_min_size = 6
    max_rooms = 30
    max_monsters_per_room = 3
    ##import tileset
    
    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )   #TODO make path to png not absolutely awful

    ## set up event handler
    event_handler = EventHandler()

    ## set up entities 

    player = copy.deepcopy(entity_factories.player)
    
    ## create dungeon
    game_map = generate_dungeon(
        map_width=map_width,
        map_height=map_height, 
        max_rooms=max_rooms,
        room_min_size=room_min_size,
        room_max_size=room_max_size,
        player=player,
        max_monsters_per_room=max_monsters_per_room,
    )

    ## initialize engine
    engine = Engine(
        event_handler = event_handler,
        game_map = game_map,
        player = player
    )

    ## define screen settings
    terminal = tcod.context.new_terminal(
        columns = screen_width,
        rows = screen_height,
        tileset = tileset,
        title = "Yet Another Roguelike Tutorial",
        vsync = True,
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
            events = tcod.event.wait()
            engine.handle_events(events)


if __name__ == "__main__":
    main()
    