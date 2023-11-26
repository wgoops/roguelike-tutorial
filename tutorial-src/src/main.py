#!/usr/bin/env python3
import tcod 
from engine import Engine
from entity import Entity
from input_handlers import EventHandler

def main(): 

    ##set screen settings 
    screen_width = 80
    screen_height = 50
    
    player_x = int(screen_width / 2)
    player_y = int(screen_height / 2)

    ##import tileset
    
    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )   #TODO make path to png not absolutely awful

    ## set up event handler
    event_handler = EventHandler()

    ## set up entities

    player = Entity(
        x = int(screen_width/2),
        y = int(screen_height/2),
        char = "@",
        color = (255,255,255)
    )

    npc = Entity(
        x = int(screen_width/2),
        y = int(screen_height/2 - 5),
        char = "@",
        color = (255,255,0)
    )
    
    entities = {npc, player} 

    engine = Engine(
        entities = entities, 
        event_handler = event_handler,
        player = player
    )

    #define screen settings
    terminal = tcod.context.new_terminal(
        columns = screen_width,
        rows = screen_height,
        tileset = tileset,
        title = "Yet Another Roguelike Tutorial",
        vsync = True,
    )
    
    #create screen
    with terminal as context: 
        root_console = tcod.Console(screen_width, screen_height, order="F")
        
        ## SET UP GAME LOOP, VERY IMPORTANT
        while True: 

            # DRAW CURRENT FRAME 
            engine.render(
                console = root_console, 
                context = context
            )
            events = tcod.event.wait()
            engine.handle_events(events)
            

if __name__ == "__main__":
    main()
    