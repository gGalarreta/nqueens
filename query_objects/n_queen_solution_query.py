from models.n_queen import  NQueenSolution

class NQueenSolutionQuery():

  @classmethod
  def find_board_solutions(cls, board_id):
    return NQueenSolution.query.filter_by(owner_id=1)