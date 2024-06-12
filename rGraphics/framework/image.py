import sys, asyncio
import sdl2.ext
from rGraphics.subs.object import object
from rGraphics.framework.bmp_convert import bmpconvert
class image:
    def create_instance(self, path, size=None):
        if not size:
            size = (100,100)
        conf_path= bmpconvert().convert_to_bmp(path)
        object_properties = {
            'size': size,
            'opt_image': conf_path,
            'voxel-compliant':False,
            'space':'2' 
        }
        return object(object_properties)