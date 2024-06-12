from rGraphics import rgraphic
import os

engine = rgraphic(title="HelloWorld")
display = engine.display((1000,550), '2D')

imageHandler = engine.imageHandler()
Object1 = imageHandler.create_instance(os.path.join('test_assets','test1.png'), size=(10,10))

Object1.position((200,250))
display.load_object(Object1)

engine.run_program(display)