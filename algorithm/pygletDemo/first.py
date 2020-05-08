import pyglet
from pyglet.window import key

window = pyglet.window.Window()

label = pyglet.text.Label('hello world',
                          font_name='Times New Roman',
                          font_size=36,
                          x = window.width//2,
                          y = window.height//2,
                          anchor_x='center',
                          anchor_y='center')

# @window.event
# def on_draw():
#     window.clear()
#     label.draw()

@window.event
def on_key_press(symbol, modifiers):
    print('A key was pressed')
    if symbol == key.A:
        print('A is press')

from pyglet.window import mouse

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        print('The left mouse button was pressed.')
    print(x,y)
@window.event
def on_draw():
    window.clear()
pyglet.app.run()