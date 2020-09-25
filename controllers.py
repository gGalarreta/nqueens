from app import app
from flask import render_template
from services.algorithm.n_queen_service import NQueenService

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/nqueens/backtraking/<int:size>')
def n_queens_backtracking(size):
  n_queen_service_object = NQueenService(size, size)
  n_queen_service_object.play()
  solutions = n_queen_service_object.solutions()
  return render_template('nqueens/backtracking/index.html', solutions = solutions[size], size_board = size)

@app.route('/nqueens/backtraking/range_solution/<int:minimum_size>/<int:maximum_size>')
def n_queens_backtracking_full_range_solution(minimum_size, maximum_size):
  n_queen_service_object = NQueenService(minimum_size, maximum_size)
  n_queen_service_object.play()
  solutions = n_queen_service_object.solutions()
  if not bool(solutions):
    return render_template('nqueens/invalid.html')
  else:
    return render_template('nqueens/backtracking/range_solution.html', solutions = solutions, minimum_size_board = minimum_size, maximum_size_board = maximum_size + 1)
