import sys
import sdl2.ext
class display:
    def __init__(self, settings):
        self.wsize = settings[0]
        self.title = settings[1][6:].strip()

        sdl2.ext.init()
        window = sdl2.ext.Window(self.title, size=self.wsize)
        window.show()
        
        processor = sdl2.ext.TestEventProcessor()
        processor.run(window)
    
    def load_object(self):
        return 