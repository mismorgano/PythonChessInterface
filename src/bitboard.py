from dataclasses import dataclass, field
from enum import auto, IntEnum
from ctypes import c_uint64


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


@dataclass
class BitBoard(c_uint64):
    pass


@dataclass
class PieceBitBoard:
    piece: str
    bitboard: BitBoard = 0

    def __str__(self):
        # each index correspond to a square on the board from 0 to 63 which we use to determine if there is a piece
        # in the bitboard using the & operator, 1 when there is and 0 when there is not
        ranks = [
            f"""{8 - rank}  {" ".join(f"{self.piece if self._get_bit(rank * 8 + file) else 0}"
                                      for file in range(8))}""" for rank in range(8)]
        ranks += ['']
        ranks += [f'   {" ".join("a b c d e f g h".split())}']
        ranks += ['']
        ranks += [f'   BitBoard: {self.bitboard}']
        ranks += ['']
        return '\n'.join(ranks)

    def _get_bit(self, square: BoardSquare):
        """Determines if BitBoard has a 1 at the given square."""
        return self.bitboard & (1 << square)

    def set_square(self, square: BoardSquare):
        """Set BitBoard bit to 1 at given square"""
        self.bitboard |= (1 << square)

    def pop_square(self, square: BoardSquare):
        """Set BitBoard bit to 0 at given square"""
        self.bitboard = self.bitboard ^ (1 << square) if self._get_bit(square) else 0


def main():
    bishop_bit_board = PieceBitBoard(piece='B', bitboard=10)
    print(bishop_bit_board)
    bishop_bit_board.set_square(BoardSquare.C3)
    bishop_bit_board.set_square(BoardSquare.E4)
    bishop_bit_board.set_square(BoardSquare.F2)
    bishop_bit_board.set_square(BoardSquare.H1)
    bishop_bit_board.pop_square(BoardSquare.H1)

    print(bishop_bit_board)


if __name__ == '__main__':
    main()
