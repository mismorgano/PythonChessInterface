from dataclasses import dataclass, field


class BitBoard(int):
    def __new__(cls, value=0):
        # Use __new__ to initialize the instance
        return super().__new__(cls, value)

    def get_bit(self, index):
        """Determines if BitBoard has a 1 at the given index."""
        return self & (1 << index)


@dataclass
class PieceBitBoard:
    piece: str
    bitboard: BitBoard = field(default_factory=BitBoard)

    def __post_init__(self):
        self.bitboard = BitBoard(self.bitboard)

    def __repr__(self):
        # each index correspond to a square on the board from 0 to 63 which we use to determine if there is a piece
        # in the bitboard using the & operator, 1 when there is and 0 when there is not
        ranks = [
            f"""{8 - rank}  {" ".join(f"{self.piece if self.bitboard.get_bit(rank * 8 + file) else 0}"
                                      for file in range(8))}""" for rank in range(8)]
        ranks += ['']
        ranks += [f'   {" ".join("a b c d e f g h".split())}']
        ranks += ['']
        ranks += [f'   BitBoard: {self.bitboard}']
        return '\n'.join(ranks)
