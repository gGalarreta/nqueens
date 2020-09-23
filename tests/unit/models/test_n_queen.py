from models.n_queen import NQueen, NQueenSolution
import pytest

@pytest.fixture(scope='module')
def new_n_queen():
  return NQueen.create(board_size=4, algorithm_name='backtracking')

@pytest.fixture(scope='module')
def new_n_queen_solution():
  return NQueenSolution(value='1,3,0,2', owner=new_n_queen())

def test_new_n_queen(new_n_queen):
  assert isinstance(new_n_queen.board_size, str)
  assert new_n_queen.board_size == '4'
  assert new_n_queen.board_size != ''
  assert isinstance(new_n_queen.algorithm_name, str)
  assert new_n_queen.algorithm_name == 'backtracking'
  assert new_n_queen.algorithm_name != ''
  solution_four_queen = [[1,3,0,2],[2,0,3,1]]
  assert new_n_queen.build_nqueen_solutions(solution_four_queen) is True

def test_new_n_queen_solution(new_n_queen_solution):
  assert isinstance(new_n_queen_solution.value, str)
  assert new_n_queen_solution.value == '1,3,0,2'
  assert new_n_queen_solution.value != ''
  assert new_n_queen_solution.owner_id != ''