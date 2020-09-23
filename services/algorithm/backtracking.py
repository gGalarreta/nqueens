import copy
from services.algorithm.constants import DEFAULT_VECTOR_VALUE

class Backtracking():
  def __init__(self, vector, board_size):
    self.__vector = vector
    self.__board_size = board_size
    self.__solutions = []

  def call(self):
    try:
      if self.__board_size < 1: return False

      self.__n_queen(self.__vector, 0)
    except:
      return False
    return True

  def solution(self):
    return self.__solutions

  def __n_queen(self, vector, movement):
    if movement > (self.__board_size - 1):
      return False

    vector[movement] = -1
    while vector[movement] != self.__board_size:
      vector[movement] = vector[movement] + 1
      if self.__is_solution(vector):
        self.__solutions.append(copy.deepcopy(vector))
      if self.__valid_board(vector, movement) is True: self.__n_queen(vector, movement + 1)

  def __valid_board(self, vector, movement):
    for col in range(movement):
      if (
        vector[col] == vector[movement] or \
        vector[col] == DEFAULT_VECTOR_VALUE or \
        vector[movement] == DEFAULT_VECTOR_VALUE or \
        vector[col] == self.__board_size or \
        vector[movement] == self.__board_size or \
        abs(vector[col] - vector[movement]) == abs(col - movement)
      ):
        return False
    return True

  def __is_solution(self, vector):
    success = True
    for row in range(self.__board_size):
      success = success and self.__valid_board(vector, row)
    return success