from rGraphics.framework.display import display
from rGraphics.framework.image import image
class rgraphic:
    def __init__(self, title=None):
        self.title = title
        self.wsize = None

        self.disinfo = None
    def display(self, window_size):
        information = []
        information.append(window_size)
        if self.title != None:
            information.append('title:'+str(self.title))
        else:
            information.append('title:None')
        confirmed = display(information); self.disinfo = confirmed
        return confirmed
    def imageHandler(self):
        return image()