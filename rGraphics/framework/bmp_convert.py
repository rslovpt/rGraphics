#CREATED BY @PROMETEU on Reddit!
import os, random, string, time
from PIL import Image
import numpy as np
class bmpconvert:
    def convert_to_bmp(self, image):
        generated_id = ''.join(random.choices(string.ascii_uppercase, k=random.randint(7,50)))
        image = Image.open(image).save(os.path.join('rGraphics', 'bitmap_cache',str(generated_id)+'.bmp'))
        path = os.path.join('rGraphics', 'bitmap_cache',str(generated_id)+'.bmp')
        return path