import pyglet


window = pyglet.window.Window(900, 500)
batch = pyglet.graphics.Batch()
assets_path = ['../assets/JohnPablokCburnettChessSet/PNGs/No shadow/128h']

## loading resources
pyglet.resource.path = assets_path
pyglet.resource.reindex()

gray_dark_tile = pyglet.resource.image('square gray dark _png_128px.png')
gray_dark_tile.anchor_x = -10
gray_dark_tile.anchor_y = -10

tiles = []

pyglet.sprite.Sprite(gray_dark_tile, 450, 250, batch=batch)

# tiles[0].x = 0
# tiles[0].y = 0

@window.event
def on_draw():
    batch.draw()





# class ChessInterface(pyglet.event.EventDispatcher):
    
#     def __init__(self,color='black', *args,**kwargs):
#         print(args, kwargs)
#         super().__init__(*args,**kwargs)
        

# window = ChessInterface(width=500, height=500, color='green')

pyglet.app.run()