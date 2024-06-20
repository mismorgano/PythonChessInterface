from pyglet import shapes
import pyglet.resource
from pyglet.image import AbstractImage
from pyglet.sprite import Sprite

from fennotation import Fen



class ChessBoard:
    """Represent and show the state of the board"""

    def __init__(
        self, x: int, y: int, tile_size: int, batch: pyglet.graphics.Batch
    ) -> None:
        """Initialize the board given xy coordinates"""
        self._x = x
        self._y = y
        self._batch = batch
        
        self._tile_size = tile_size
        self._pieces = []
        self._active_piece = (None, None)

    

        # print(pos)
        # print(len(self._pieces))

    

    def __getitem__(self, index):
        return self._pieces[index]

    