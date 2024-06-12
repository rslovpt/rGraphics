import sys
import sdl2.ext
class runtime:
    def __init__(self, display):
        if display.__class__.__name__ == 'display':
            self.display = display
        else:
            print("Invalid Screen Parameters")
        return
    def init_rt(self):
        processor = sdl2.ext.TestEventProcessor()
        processor.run(self.display.retrive_wdata())
    def init_dobl_rt(self):
        run = True
        while run:
            events = sdl2.ext.get_events()
            for event in events:
                if event.type == sdl2.SDL_QUIT:
                    run=False
                    break
            self.display.retrive_wdata().refresh()   