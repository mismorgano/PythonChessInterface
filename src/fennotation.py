class Fen:
    """Represent the Fen notation of the board state"""

    def __init__(self, fen: str) -> None:
        """Constructs the board state given a valid fen string"""
        self._fen = fen
        self._board = []
        ranks = fen.split("/")
        for rank in ranks:
            file = []
            for _, piece in enumerate(rank):
                if not piece.isdigit():
                    file.append(piece)
                else:
                    file += [None] * int(piece)
            self._board.append(file)
        # reversed to use [rank][file] indexing
        self._board = list(reversed(self._board))
        # print(self._board)

    def __getitem__(self, position):
        return self._board[position]


fen = Fen("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")

# print(list(reversed(fen._board)))
# print(len(fen._board))
