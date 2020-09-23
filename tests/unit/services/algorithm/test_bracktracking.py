from tests.configuration_test import *

def test_call_method(valid_backtracking_instance, invalid_backtracking_instance):
  assert valid_backtracking_instance.call() is True
  assert invalid_backtracking_instance.call() is False

def test_solution_method(valid_backtracking_instance, valid_eigh_backtracking_instance, invalid_backtracking_instance):
  solution_four_queen = [[1,3,0,2],[2,0,3,1]]
  solution_incomplete_queen = [[1,3,0,2]]
  solution_invalid_queen = []

  valid_backtracking_instance.call()
  valid_eigh_backtracking_instance.call()

  assert valid_backtracking_instance.solution() == solution_four_queen
  assert valid_backtracking_instance.solution() != solution_incomplete_queen
  assert invalid_backtracking_instance.solution() == solution_invalid_queen
  assert len(valid_backtracking_instance.solution()) == 2
  assert len(valid_eigh_backtracking_instance.solution()) == 92
