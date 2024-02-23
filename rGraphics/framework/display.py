import sys
import sdl2.ext
class display:
    def __init__(self, settings):
        self.wsize = settings[0]
        self.title = settings[1][6:].strip()

        sdl2.ext.init()
        self.window = sdl2.ext.Window(self.title, size=self.wsize)
        self.window.show()
    
    def load_object(self, object):
        attributes=object.bitattributes()
        print(attributes)
    
    def retrive_wdata(self):
        return self.window