from services.algorithm.backtracking import Backtracking
from services.algorithm.constants import *
from query_objects.n_queen_query import NQueenQuery
from query_objects.n_queen_solution_query import NQueenSolutionQuery
from models.n_queen import NQueen

class NQueenService():
  def __init__(self, minimum_board_size, maximum_board_size):
    self.__solutions = {}
    self.__minium_board_size = minimum_board_size
    self.__maxium_board_size = maximum_board_size

  def play(self):
    if self.__valid_board() is not True: return False

    try:
      for board in range(self.__minium_board_size, self.__maxium_board_size + 1):
        board_solution = NQueenQuery.find_board(board)
        if board_solution:
          self.__solutions[board] = self.__find_board_solutions(board_solution.id)
          return True

        n_queen_backtracking = Backtracking(self.__init_vector(board), board)
        n_queen_backtracking.call()
        n_queen = NQueen.create(board_size=board, algorithm_name='backtracking')
        n_queen.build_nqueen_solutions(n_queen_backtracking.solution())
        self.__solutions[board] = n_queen_backtracking.solution()
    except:
      return False
    return True

  def solutions(self):
    return self.__solutions

  def __init_vector(self, board_size):
    return [DEFAULT_VECTOR_VALUE] * board_size

  def __find_board_solutions(self, board_id):
    result = []
    for solution in NQueenSolutionQuery.find_board_solutions(board_id):
      value = solution.value.split(',')
      result.append(list(map(lambda x: int(x), value)))
    return result

  def __valid_board(self):
    return self.__minium_board_size > 1 and \
      self.__maxium_board_size > 1 and \
      self.__minium_board_size <= self.__maxium_board_size
