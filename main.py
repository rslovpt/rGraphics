from rGraphics import rgraphic

engine = rgraphic(title="HelloWorld")
display = engine.display((600,250), '2D')

imageHandler = engine.imageHandler()
Object1 = imageHandler.create_instance('test_assets\Test1.png', size=(50,50))

Object1.position((200,250))
display.load_object(Object1)

engine.run_program(display)