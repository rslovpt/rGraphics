import sys, time, os
import sdl2.ext
def clear_bitmap_cache() -> None:
    filecount=0
    for i,v in enumerate ( os.listdir(os.path.join('rGraphics','bitmap_cache')) ):
        if os.path.exists(os.path.join('rGraphics', 'bitmap_cache', v)) is True: os.remove(os.path.join('rGraphics', 'bitmap_cache', v))
        filecount = v
class display:
    def __init__(self, settings):
        self.wsize = settings[0]
        self.title = settings[1][6:].strip()

        clear_bitmap_cache()

        sdl2.ext.init()
        self.window = sdl2.ext.Window(self.title, size=self.wsize)
        self.window.show()

        self.fc=sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)
        self.rdr=self.fc.create_sprite_render_system(self.window)
        self.bmp_rsc = sdl2.ext.Resources(__file__, '../bitmap_cache')

    def load_object(self, object):
        attributes=object.bitattributes()
        ld_object=None
        if attributes['objimage'] != None:
            self.bmp_rsc = sdl2.ext.Resources(__file__, '../bitmap_cache')
            path_name=attributes['objimage'].split("\ ".strip())[-1]
            ld_object=self.fc.from_image(self.bmp_rsc.get_path(path_name))
            ld_object.position = attributes['objposition']
            self.rdr.render(ld_object)
    
    def retrive_wdata(self):
        return self.window