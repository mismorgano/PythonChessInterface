from chesspiece.piece import Piece, ChessPiece

from position import Postition

from chesspiece.piece import ChessPieceType

class PawnPiece(ChessPiece):
    def __init__(self, color):
        super().__init__(color)
        self.type = ChessPieceType.PAWN

    

class Pawn(Piece):
    
    def __init__(self, rank, file, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = Postition(Rank=rank, File=file)