import sys
import sdl2.ext
class object:
    def __init__(self, properties):
        self.obj_size = properties['size']
        if properties['opt_image']:
            self.opt_image = properties['opt_image']
        self.obj_spaciary = properties['space']
        self.voxel_complt = properties['voxel-compliant']
        self.obj_position = (0,0)
    def position(self, position : tuple):
        self.obj_position = position
    def bitattributes(self):
        attr = {
            'objsize':self.obj_size,
            'objposition':self.obj_position,
            'objspaciary':self.obj_spaciary,
            'voxelized':False
        }
        if self.opt_image != None:
            attr['objimage'] = self.opt_image
        else:
            pass
        return attr