import platform
import ctypes
from fennotation import Fen
import pyglet
from pyglet.window import mouse

# set process DPI aware in windows
system = platform.uname()
minimum_windows_version_required = 6  # Windows Vista
if (
    system.system == "Windows"
    and int(system.release) >= minimum_windows_version_required
):
    ctypes.windll.user32.SetProcessDPIAware()

# Defined constants
TILE_SIZE = 80

WIDTH = 8 * TILE_SIZE
HEIGHT = 8 * TILE_SIZE


window = pyglet.window.Window(
    width=WIDTH, height=HEIGHT, caption="My awesome chess Interface", resizable=False
)
batch = pyglet.graphics.Batch()

# from board import ChessBoard
from render import render, setup, deactivate, activate, ACTIVE_PIECE

# chess_board = ChessBoard(0, 0, 80, batch)
# chess_board.setup(Fen("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"))

render(0, 0, TILE_SIZE, None, batch)
fen = Fen("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")
setup(0, 0, TILE_SIZE, fen, batch)


@window.event
def on_draw():
    window.clear()
    batch.draw()


@window.event
def on_mouse_press(x, y, button, modifiers):
    global ACTIVE_PIECE

    ACTIVE_PIECE = deactivate(x, y, TILE_SIZE, fen, batch)
    


@window.event
def on_mouse_release(x, y, button, modifiers):
    global ACTIVE_PIECE

    ACTIVE_PIECE = activate(x, y, fen, TILE_SIZE, batch)


@window.event
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    if buttons & mouse.LEFT:
        print(ACTIVE_PIECE)
        active = ACTIVE_PIECE[0]
        
        if active:
            active.x = x
            active.y = y
        # chess_board[rank][file] = active
        # chess_board.fen[rank][file] = chess_board._active_piece[1]


if __name__ == "__main__":
    pyglet.app.run()
