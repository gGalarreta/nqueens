# from models.n_queen import NQueen, NQueenSolution
from services.algorithm.backtracking import Backtracking
# from services.algorithm.n_queen_service import NQueenService
import pytest

# @pytest.fixture
# def new_n_queen():
#   return NQueen.create(board_size=4, algorithm_name='backtracking')

# @pytest.fixture
# def new_n_queen_solution():
#   return NQueenSolution(value='1,3,0,2', owner=new_n_queen())

@pytest.fixture
def valid_backtracking_instance():
  board_size = 4
  vector = [-1] * board_size
  return Backtracking(vector, board_size)

@pytest.fixture
def invalid_backtracking_instance():
  board_size = -4
  vector = [-1] * board_size
  return Backtracking(vector, board_size)

@pytest.fixture
def valid_eigh_backtracking_instance():
  board_size = 8
  vector = [-1] * board_size
  return Backtracking(vector, board_size)

# @pytest.fixture
# def valid_n_queen_service():
#   board_size = 4
#   return NQueenService(board_size, board_size)

# @pytest.fixture
# def invalid_negatives_size_n_queen_service():
#   board_size = -4
#   return NQueenService(board_size, board_size)

# @pytest.fixture
# def invalid_range_n_queen_service():
#   minimum_board_size = 10
#   maximum_board_size = 2
#   return NQueenService(minimum_board_size, maximum_board_size)

# @pytest.fixture
# def valid_four_queen_service():
#   board_size = 4
#   return NQueenService(board_size, board_size)

# @pytest.fixture
# def valid_eigh_queen_service():
#   board_size = 8
#   return NQueenService(board_size, board_size)