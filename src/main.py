import pyglet
import platform
import ctypes
import pyglet.resource as resource



import os

system = platform.uname()
minumun_windows_version_required = 6 # Windows Vista
if system.system == 'Windows' and int(system.release) >= minumun_windows_version_required:
    ctypes.windll.user32.SetProcessDPIAware()

TILE_SIZE = 80
    
WIDTH = 8*TILE_SIZE
HEIGHT = 8*TILE_SIZE


window = pyglet.window.Window(width=WIDTH, height=HEIGHT, caption='My awesome chess Interface',  resizable=True)
# window = pyglet.window.Window(fullscreen=True, caption='My awesome chess interface')

foreground = pyglet.graphics.Group(order=1)
f = pyglet.graphics.Group(order=1)
background = pyglet.graphics.Group(order=0)
print(foreground == background)

from board import  BoardBackground,make_board_and_pawns, get_files, ChessBoard

assets_path = ['../assets/JohnPablokCburnettChessSet/PNGs/No shadow/128h']

# ## loading resources
# resource.path = assets_path
# #resource.path.append(r'assets/JohnPablokCburnettChessSet/PNGs/No shadow/1x')
# resource.reindex()
print(resource.path)
# for file in get_files((os.path.normpath(os.path.join(os.path.dirname(__file__), assets_path[0])))):
#     print(file.name)
tiles = []
# b_bishop = resource.image('b_bishop_1x.png')
# b_bishop_ns = resource.image('b_bishop_png_128px.png')

batch = pyglet.graphics.Batch()
#b_bishop_s = pyglet.sprite.Sprite(b_bishop, x=0, y=0, batch=batch, group=foreground)
# b_bishop_s_ns = Piece(b_bishop_ns, x=0, y=0, batch=batch, group=foreground)
background_color = pyglet.shapes.Rectangle(x=0, y=0, width=WIDTH, height=HEIGHT, batch=batch, group=background, color=(90, 160,130))

# b_bishop_s_ns.scale = 0.4

# gray tiles
# gray_dark_tile = resource.image('square gray dark _png_128px.png')
# gray_light_tile = resource.image('square gray light _png_128px.png')

# b_pawn = resource.image('b_pawn_png_128px.png')
# board_background = BoardBackground(gray_light_tile, gray_dark_tile)
# board_background.make_board(0,0, batch=batch, group=background)


# background =make_board_and_pawns(gray_light_tile, gray_dark_tile, b_pawn, batch, foreground)
# board_background = BoardBackground()
# board_background.make_board(0, 0, batch=batch, group=foreground)


chess_board = ChessBoard(0, 0, 80, batch)
chess_board.setup('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR')
@window.event
def on_draw():
    window.clear()
    batch.draw()

@window.event
def on_resize(width, heigh):
    background_color.width = width
    background_color.height = heigh

if __name__ == '__main__':
    pyglet.app.run()
    
    
