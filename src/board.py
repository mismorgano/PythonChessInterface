from ctypes import sizeof
from pyglet import shapes
from chesspiece.piece import Piece, ChessPieceType
from chesspiece.pawn import PawnPiece
from pyglet.resource import image
import pyglet.resource 
from pyglet.image import AbstractImage
from pyglet.sprite import Sprite
import os
import sys

path = "../assets/JohnPablokCburnettChessSet/PNGs/No shadow/128h"
real_path = os.path.normpath(os.path.join(os.path.dirname(__file__), path))

assets_path = ['../assets/JohnPablokCburnettChessSet/PNGs/No shadow/128h']
# pyglet.resource.path += assets_path
# pyglet.resource.reindex()
# print(pyglet.resource.path)

loader =    pyglet.resource.Loader(assets_path[0])
print(loader.path, )
print(loader.location('square gray dark _png_128px.png').path)
gray_dark_tile = loader.image('square gray dark _png_128px.png')
gray_light_tile = loader.image('square gray light _png_128px.png')

## black pieces

b_bishop = loader.image('b_bishop_png_128px.png')
b_king =loader.image('b_king_png_128px.png')
b_knight =loader.image('b_knight_png_128px.png')
b_pawn = loader.image('b_pawn_png_128px.png')
b_queen = loader.image('b_queen_png_128px.png')
b_rook = loader.image('b_rook_png_128px.png')

## white pieces
w_bishop= loader.image('w_bishop_png_128px.png')
w_king = loader.image('w_king_png_128px.png')
w_knight = loader.image('w_knight_png_128px.png')
w_pawn = loader.image('w_pawn_png_128px.png')
w_queen = loader.image('w_queen_png_128px.png')
w_rook = loader.image('w_rook_png_128px.png')

def center_image(image: AbstractImage):
    image.anchor_x = image.width//2
    image.anchor_y = image.height//2

for piece in [b_bishop, b_king, b_knight, b_pawn, b_queen, b_rook]:
    center_image(piece)

for piece in [w_bishop, w_king, w_knight, w_pawn, w_queen, w_rook]:
    center_image(piece)

class BoardBackground:
    def __init__(
        self,
        light_tile: AbstractImage = gray_light_tile,
        dark_tile: AbstractImage=gray_dark_tile,
    ) -> None:
        self.light_tile = light_tile
        self.dark_tile = dark_tile
        self.tiles = []

    def make_board(self, x, y, batch, group=None):
        # width = self.dark_tile.get_image_data().width
        # height = self.dark_tile.get_image_data().height
        width, height = 64, 64

        for rank in range(8):
            for file in range(8):
                # print(x_pos, y_pos)
                if (rank + file) % 2 == 0:
                    color = (180, 170, 230)
                    img = self.dark_tile
                else:
                    color = (80, 50, 70)
                    img = self.light_tile
                
                tile = Sprite(img=img, batch=batch, group=group)                
                tile.scale = 0.5                
                x_pos = x + rank * width
                y_pos = y + file * height
                # print(tile.width)
                tile.x = x_pos
                tile.y = y_pos
                square = pyglet.shapes.Rectangle(x_pos, y_pos, width, height, color, batch=batch)
                self.tiles.append(square)


class Board:
    def __init__(self, x, y, size, assets_path=None) -> None:
        pyglet.resource.path.append(assets_path)
        pyglet.resource.reindex()

        self.pieces: list[Piece] = []
        for file in get_files(assets_path=assets_path):
            img = image(name=file.name)
            self.pieces.append(img)


def get_files(assets_path: os.PathLike):
    with os.scandir(assets_path) as it:
        for entry in it:
            if entry.is_file():
                yield entry


def make_board_and_pawns(white , dark, pawn:AbstractImage, batch, group):
    print(pawn.get_image_data())
    board_background = BoardBackground(white, dark)
    board_background.make_board(0, 0, batch, group)
    pawn.anchor_x = pawn.width/2
    pawn.anchor_y = pawn.height/2
    fp = Sprite(img=pawn, x=32, y=32, batch=batch, group=group)
    fp.scale = 0.5

    board_background.tiles.append(fp)
    return board_background

# pyglet.resource.path = [real_path]
# pyglet.resource.reindex()
# print(pyglet.resource.path)
# for file in get_files(real_path):
#     if 'square' in file.name:
#         img = image(name=file.name)

#         print(img.get_image_data().width, file.name)



class ChessBoard:
    img_pieces = {
        'b': b_bishop,        
        'k': b_king,
        'n': b_knight,
        'p': b_pawn,
        'q': b_queen,
        'r': b_rook,
        'B': w_bishop,
        'K': w_king,
        'N': w_knight,
        'P': w_pawn,
        'Q': w_queen,
        'R': w_rook,
    }
    
    def __init__(self, x:int, y:int, tile_size:int, batch) -> None:
        self._x = x
        self._y = y
        self._batch = batch
        self._group_background = pyglet.graphics.Group(order=0)
        self._group_foreground = pyglet.graphics.Group(order=1)
        self._tiles = [[shapes.Rectangle]*8 for i in range(8)]
        self._tile_size = tile_size
        self._pieces = []


    def setup(self, fen:str):
        self.fen = fen
        ranks = fen.split('/')
        for r in ranks:
            print(r)
        print(ranks)
        self.make_board()
        size = self._tile_size
        
        pos = 0
        for rank in range(8):
            for _, piece in enumerate(ranks[rank]):
                
                if not str.isdigit(piece):
                    
                    img = self.img_pieces[piece]
                    i, j = 7 - pos//8, 7- pos %8
                    
                    x, y = self._x + size*j + size/2, self._y + size*i + size/2
                    print(i, j, x, y,piece)
                    piece = pyglet.sprite.Sprite(img, x, y, batch=self._batch, group=self._group_foreground)
                    piece.scale = 0.5
                    self._pieces.append(piece)
                    pos += 1
                else:
                    pos += int(piece)
            # match self.black_pieces[i].type:
            #     case ChessPieceType.PAWN:
            #         img = self.img_pieces['p']
            #         x, y = self._x + size*i + size/2, self._y + 3*size/2
            #         print(img.width)
            
        print(pos)
            
    
    def make_board(self) -> None:
        size = self._tile_size
        for rank in range(8):
            for file in range(8):
                x, y = self._x + size * file, self._y + size * rank
                if (rank + file) % 2 == 0:
                    color = (80, 50, 70)
                else:
                    color = (180, 170, 230)
                tile = shapes.Rectangle(x, y, size, size, color, self._batch, self._group_background)

                self._tiles[rank][file] = tile
