from pyglet import image
from position import Postition

from enum import Enum, auto
class ChessPieceType(Enum):
    PAWN = auto()
    BISHOP = auto()
    KNIGHT = auto()
    ROOK = auto()
    QUEEN = auto()
    KING = auto()


class ChessPiece:
    def __init__(self, color):
        self.color = color
        self.is_alive = True
        self.position: Postition = None
        self.type: ChessPieceType = None

    def __repr__(self):
        return f"{self.color} {type(self).__name__}"

    def get_possible_moves(self):
        """
        Returns a list of possible moves for the piece
        """
        raise NotImplementedError("This method must be implemented by the subclass")

    def move(self, position: Postition):
        """
        Moves the piece to the given position
        """
        self.position = position

    def is_valid_move(self, board, position: Postition):
        """
        Returns True if the given position is a valid move for the piece
        """
        possible_moves = self.get_possible_moves()
        if position not in possible_moves:
            return False
        # Check if the move puts the player's own king in check
        king = board.get_king(self.color)
        if king.is_in_check_after_move(self, position):
            return False
        return True


class Piece(image.AbstractImage):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = None


    