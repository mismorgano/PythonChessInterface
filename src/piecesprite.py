
from pyglet import sprite

class ChessPieceSprite(sprite.Sprite):
    
    def __init__(self, piece, image):
        super().__init__(image)
        self.piece = piece