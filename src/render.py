import pyglet
from pyglet.image import AbstractImage
from pyglet import shapes
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


GROUP_BACKGROUND = pyglet.graphics.Group(order=0)
GROUP_FOREGROUND = pyglet.graphics.Group(order=1)
GROUP_ACTIVE_PIECE = pyglet.graphics.Group(order=1, parent=GROUP_FOREGROUND)

TILES = [[shapes.Rectangle] * 8 for i in range(8)]

DARK_COLOR = (80, 50, 70)
LIGHT_COLOR = (180, 170, 230)

PIECES = []

ACTIVE_PIECE = (None, None)

def make_board(x: int, y: int, tile_size: int, batch) -> None:
    size = tile_size
    for rank in range(8):
        for file in range(8):
            _x, _y = x + size * file, y + size * rank
            if (rank + file) % 2 == 0:
                color = DARK_COLOR
            else:
                color = LIGHT_COLOR
            tile = shapes.Rectangle(_x, _y, size, size, color, batch, GROUP_BACKGROUND)

            TILES[rank][file] = tile


def setup(x, y, tile_size, fen: Fen, batch):
    size = tile_size

    pos = 0
    # print(fen._board)
    for rank in range(8):
        row = []
        for file in range(8):
            piece = fen[rank][file]

            if piece is not None:
                img = img_pieces[piece]
                i, j = rank, file

                _x, _y = x + size * j + size / 2, y + size * i + size / 2
                # print(i, j, x, y,file, piece)
                piece = Sprite(img, _x, _y, batch=batch, group=GROUP_FOREGROUND)
                piece.scale = 0.5
                row.append(piece)
                pos += 1
            else:
                row.append(None)
                pos += 1

        PIECES.append(row)


def render(x, y, tile_size, board, batch):
    make_board(x, y, tile_size, batch)


def deactivate(x, y, tile_size, fen, batch):
    TILE_SIZE = tile_size
    file, rank = x // TILE_SIZE, y // TILE_SIZE
    piece = fen[rank][file]
    global ACTIVE_PIECE
    if piece is not None:
        apiece = img_pieces[piece]
        apiece = Sprite(apiece, batch=batch, group=GROUP_ACTIVE_PIECE)
        apiece.scale = 0.5
        apiece.x = x
        apiece.y = y
        
        ACTIVE_PIECE = (apiece, fen[rank][file])
        PIECES[rank][file] = None
        fen[rank][file] = None
        # print(ACTIVE_PIECE)
        change_color_tile(rank, file, 0)
    return ACTIVE_PIECE


def activate(x, y, fen, tile_size, batch):
    TILE_SIZE = tile_size
    file, rank = x // TILE_SIZE, y // TILE_SIZE
    global ACTIVE_PIECE
    active = ACTIVE_PIECE
    if active != (None, None):
        img = img_pieces[active[1]]
        piece = pyglet.sprite.Sprite(
            img, x, y, batch=batch, group=GROUP_FOREGROUND
        )
        piece.x = TILE_SIZE * file + TILE_SIZE / 2
        piece.y = TILE_SIZE * rank + TILE_SIZE / 2
        piece.scale = 0.5
        PIECES[rank][file] = piece  # should create another Sprite with foreground
        fen[rank][file] = active[1]
        change_color_tile(rank, file, 1)
        ACTIVE_PIECE = None, None
    return ACTIVE_PIECE


def change_color_tile(rank, file, n):
    active_tile = TILES[rank][file]

    r, g, b, _ = active_tile.color
    active_tile.color = (r, g, b, 255 if n else 150)
