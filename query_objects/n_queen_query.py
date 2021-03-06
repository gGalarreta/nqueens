from models.n_queen import NQueen

class NQueenQuery():

  @classmethod
  def find_board(cls, board_size):
    return NQueen.query.filter_by(board_size=str(board_size)).first()