from app import app
from flask import render_template
from services.algorithm.n_queen_service import NQueenService

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/nqueens/backtraking/<size>')
def n_queens_backtracking(size):
  size = int(size)
  n_queen_service_object = NQueenService(size,size)
  n_queen_service_object.play()
  solutions = n_queen_service_object.solutions()
  return render_template('nqueens/backtracking/index.html', solutions = solutions[size], size_board = size)