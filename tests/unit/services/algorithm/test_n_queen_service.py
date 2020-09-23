
def test_play_method(valid_n_queen_service, invalid_negatives_size_n_queen_service, invalid_range_n_queen_service):
  assert valid_n_queen_service.play() is True
  assert invalid_negatives_size_n_queen_service.play() is False
  assert invalid_range_n_queen_service.play() is False

def test_solutions_method(valid_four_queen_service, valid_eigh_queen_service, invalid_negatives_size_n_queen_service, invalid_range_n_queen_service):
  correct_solutions = {4: [[1,3,0,2],[2,0,3,1]]}
  empty_solutions = {}

  valid_four_queen_service.play()
  valid_eigh_queen_service.play()

  assert isinstance(valid_four_queen_service.solutions(), dict)
  assert isinstance(valid_four_queen_service.solutions()[4], list)
  assert valid_four_queen_service.solutions()[4] == correct_solutions[4]
  assert invalid_negatives_size_n_queen_service.solutions() == empty_solutions
  assert invalid_range_n_queen_service.solutions() == empty_solutions
  assert len(valid_four_queen_service.solutions()[4]) == 2
  assert len(valid_eigh_queen_service.solutions()[8]) == 92