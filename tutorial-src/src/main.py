#!/usr/bin/env python3
import tcod 
from actions import EscapeAction, MovementAction
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
            root_console.print(x=player_x, y=player_y, string="@")
            context.present(root_console)
            root_console.clear()
            for event in tcod.event.wait():
                action = event_handler.dispatch(event)
                if action is None: 
                    continue
                
                if isinstance(action, MovementAction):
                    player_x += action.dx
                    player_y += action.dy
                
                elif isinstance(aciton, EscapeAction):
                    raise SystemExit()

if __name__ == "__main__":
    main()
    