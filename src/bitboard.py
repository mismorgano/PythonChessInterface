from dataclasses import dataclass, field
from enum import auto, IntEnum


# Board squares
class BoardSquare(IntEnum):
    A8 = 0
    B8 = auto()
    C8 = auto()
    D8 = auto()
    E8 = auto()
    F8 = auto()
    G8 = auto()
    H8 = auto()
    A7 = auto()
    B7 = auto()
    C7 = auto()
    D7 = auto()
    E7 = auto()
    F7 = auto()
    G7 = auto()
    H7 = auto()
    A6 = auto()
    B6 = auto()
    C6 = auto()
    D6 = auto()
    E6 = auto()
    F6 = auto()
    G6 = auto()
    H6 = auto()
    A5 = auto()
    B5 = auto()
    C5 = auto()
    D5 = auto()
    E5 = auto()
    F5 = auto()
    G5 = auto()
    H5 = auto()
    A4 = auto()
    B4 = auto()
    C4 = auto()
    D4 = auto()
    E4 = auto()
    F4 = auto()
    G4 = auto()
    H4 = auto()
    A3 = auto()
    B3 = auto()
    C3 = auto()
    D3 = auto()
    E3 = auto()
    F3 = auto()
    G3 = auto()
    H3 = auto()
    A2 = auto()
    B2 = auto()
    C2 = auto()
    D2 = auto()
    E2 = auto()
    F2 = auto()
    G2 = auto()
    H2 = auto()
    A1 = auto()
    B1 = auto()
    C1 = auto()
    D1 = auto()
    E1 = auto()
    F1 = auto()
    G1 = auto()
    H1 = auto()


class BitBoard(int):

    def get_bit(self, square: BoardSquare):
        """Determines if BitBoard has a 1 at the given square."""
        return self & (1 << square)

    def set_bit(self, square: BoardSquare):
        """Set BitBoard bit to 1 at given square"""
        return BitBoard(self | (1 << square))

    def pop_bit(self, square: BoardSquare):
        """Set BitBoard bit to 0 at given square"""
        return BitBoard(self ^ (1 << square) if self.get_bit(square) else 0)


@dataclass
class PieceBitBoard:
    piece: str
    bitboard: BitBoard = field(default_factory=BitBoard)

    def __post_init__(self):
        """Force BitBoard to be of type BitBoard."""
        self.bitboard = BitBoard(self.bitboard)

    def __str__(self):
        # each index correspond to a square on the board from 0 to 63 which we use to determine if there is a piece
        # in the bitboard using the & operator, 1 when there is and 0 when there is not
        ranks = [
            f"""{8 - rank}  {" ".join(f"{self.piece if self.bitboard.get_bit(rank * 8 + file) else 0}"
                                      for file in range(8))}""" for rank in range(8)]
        ranks += ['']
        ranks += [f'   {" ".join("a b c d e f g h".split())}']
        ranks += ['']
        ranks += [f'   BitBoard: {self.bitboard}']
        ranks += ['']
        return '\n'.join(ranks)

    def set_bit(self, square: BoardSquare):
        self.bitboard = self.bitboard.set_bit(square)

    def pop_bit(self, square: BoardSquare):
        self.bitboard = self.bitboard.pop_bit(square)


def main():
    piece = PieceBitBoard(piece='B')
    print(piece)
    piece.set_bit(BoardSquare.C3)
    piece.set_bit(BoardSquare.E4)
    piece.set_bit(BoardSquare.F2)
    piece.set_bit(BoardSquare.H1)
    piece.pop_bit(BoardSquare.H1)
    print(piece)


if __name__ == '__main__':
    main()
