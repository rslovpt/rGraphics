import sys
import sdl2.ext
from rGraphics.subs.object import object
class image:
    def create_instance(self, path, size=None):
        if not size:
            size = (100,100)
        object_properties = {
            'size': size,
            'opt_image': path,
            'voxel-compliant':False,
            'space':'2' 
        }
        return object(object_properties)