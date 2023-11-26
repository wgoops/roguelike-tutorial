#!/usr/bin/env python3
import tcod 

def main(): 

    ##set screen settings 
    screen_width = 80
    screen_height = 50
    
    ##import tileset
    
    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )   #TODO make path to png not absolutely awful
    
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
            root_console.print(x=1, y=1, string="@")
            context.present(root_console)
            for event in tcod.event.wait():
                if event.type == "QUIT":
                    raise SystemExit()

if __name__ == "__main__":
    main()
    