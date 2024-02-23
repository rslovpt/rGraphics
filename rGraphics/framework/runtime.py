import sys
import sdl2.ext
class runtime:
    def __init__(self, display):
        if display.__class__.__name__ == 'display':
            self.display = display
        else:
            print("Invalid Screen Param")
        return
    def init_rt(self):
        processor = sdl2.ext.TestEventProcessor()
        processor.run(self.display.retrive_wdata())