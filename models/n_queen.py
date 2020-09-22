from app import db

class NQueen(db.Model):
  __tablename__ = 'nqueen'
  id = db.Column(db.Integer, primary_key=True)
  board_size = db.Column(db.String(50))
  algorithm_name = db.Column(db.String(50))
  solutions = db.relationship('NQueenSolution', backref='owner')

  def build_nqueen_solutions(self, data):
    for value in data:
      value_to_string = ",".join(list(map(lambda x: str(x), value)))
      n_queen_solution = NQueenSolution(value=value_to_string, owner=self)
      db.session.add(n_queen_solution)
      db.session.commit()

  @classmethod
  def create(cls, **kw):
    obj = cls(**kw)
    db.session.add(obj)
    db.session.commit()
    return obj

class NQueenSolution(db.Model):
  __tablename__ = 'nqueen_solution'
  id = db.Column(db.Integer, primary_key=True)
  value = db.Column(db.String(50))
  owner_id = db.Column(db.Integer, db.ForeignKey('nqueen.id'))
