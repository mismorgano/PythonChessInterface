from pyglet import shapes
import pyglet.resource
from pyglet.image import AbstractImage
from pyglet.sprite import Sprite

from fennotation import Fen

assets_path = ["../assets/JohnPablokCburnettChessSet/PNGs/No shadow/128h"]

loader = pyglet.resource.Loader(assets_path[0])

## black pieces

b_bishop = loader.image("b_bishop_png_128px.png")
b_king = loader.image("b_king_png_128px.png")
b_knight = loader.image("b_knight_png_128px.png")
b_pawn = loader.image("b_pawn_png_128px.png")
b_queen = loader.image("b_queen_png_128px.png")
b_rook = loader.image("b_rook_png_128px.png")

## white pieces
w_bishop = loader.image("w_bishop_png_128px.png")
w_king = loader.image("w_king_png_128px.png")
w_knight = loader.image("w_knight_png_128px.png")
w_pawn = loader.image("w_pawn_png_128px.png")
w_queen = loader.image("w_queen_png_128px.png")
w_rook = loader.image("w_rook_png_128px.png")


def center_image(image: AbstractImage) -> None:
    """Center an Image"""
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2


# Center all the pieces
for piece in [b_bishop, b_king, b_knight, b_pawn, b_queen, b_rook]:
    center_image(piece)

for piece in [w_bishop, w_king, w_knight, w_pawn, w_queen, w_rook]:
    center_image(piece)


class ChessBoard:
    """Represent and show the state of the board"""

    img_pieces = {
        "b": b_bishop,
        "k": b_king,
        "n": b_knight,
        "p": b_pawn,
        "q": b_queen,
        "r": b_rook,
        "B": w_bishop,
        "K": w_king,
        "N": w_knight,
        "P": w_pawn,
        "Q": w_queen,
        "R": w_rook,
    }

    def __init__(
        self, x: int, y: int, tile_size: int, batch: pyglet.graphics.Batch
    ) -> None:
        """Initialize the board given xy coordinates"""
        self._x = x
        self._y = y
        self._batch = batch
        self._group_background = pyglet.graphics.Group(order=0)
        self._group_foreground = pyglet.graphics.Group(order=1)
        self._group_active_piece = pyglet.graphics.Group(
            order=1, parent=self._group_foreground
        )
        self._tiles = [[shapes.Rectangle] * 8 for i in range(8)]
        self._tile_size = tile_size
        self._pieces = []
        self._active_piece = (None, None)
        self._dark_color = (80, 50, 70)
        self._light_color = (180, 170, 230)

    def setup(self, fen: Fen):
        self.fen = fen

        self.make_board()
        size = self._tile_size

        pos = 0
        # print(fen._board)
        for rank in range(8):
            row = []
            for file in range(8):
                piece = fen[rank][file]

                if piece is not None:
                    img = self.img_pieces[piece]
                    i, j = rank, file

                    x, y = self._x + size * j + size / 2, self._y + size * i + size / 2
                    # print(i, j, x, y,file, piece)
                    piece = Sprite(
                        img, x, y, batch=self._batch, group=self._group_foreground
                    )
                    piece.scale = 0.5
                    row.append(piece)
                    pos += 1
                else:
                    row.append(None)
                    pos += 1

            self._pieces.append(row)

        # print(pos)
        # print(len(self._pieces))

    def make_board(self) -> None:
        size = self._tile_size
        for rank in range(8):
            for file in range(8):
                x, y = self._x + size * file, self._y + size * rank
                if (rank + file) % 2 == 0:
                    color = self._dark_color
                else:
                    color = self._light_color
                tile = shapes.Rectangle(
                    x, y, size, size, color, self._batch, self._group_background
                )

                self._tiles[rank][file] = tile

    def __getitem__(self, index):
        return self._pieces[index]

    def deactivate(self, x, y):
        TILE_SIZE = self._tile_size
        file, rank = x // TILE_SIZE, y // TILE_SIZE
        piece = self.fen[rank][file]
        if piece is not None:
            apiece = self.img_pieces[piece]
            apiece = Sprite(apiece, batch=self._batch, group=self._group_active_piece)
            apiece.scale = 0.5
            apiece.x = x
            apiece.y = y
            self._active_piece = (apiece, self.fen[rank][file])
            self[rank][file] = None
            self.fen[rank][file] = None

    def activate(self, x, y):
        TILE_SIZE = self._tile_size
        file, rank = x // TILE_SIZE, y // TILE_SIZE
        active = self._active_piece
        if active != (None, None):
            img = self.img_pieces[active[1]]
            piece = pyglet.sprite.Sprite(
                img, x, y, batch=self._batch, group=self._group_foreground
            )
            piece.x = TILE_SIZE * file + TILE_SIZE / 2
            piece.y = TILE_SIZE * rank + TILE_SIZE / 2
            piece.scale = 0.5
            self[rank][file] = piece  # should create another Sprite with foreground
            self.fen[rank][file] = active[1]
            self.change_color_tile(rank, file)
            self._active_piece = None, None

    def change_color_tile(self, rank, file):
        active_tile = self._tiles[rank][file]
            
        r, g, b, _ = active_tile.color
        active_tile.color = (r, g, b, 150)