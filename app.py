from flask import Flask, render_template, request, redirect, session, g
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')


db = SQLAlchemy(app)
db.create_all()

if __name__ == "__main__":
  from controllers import home
  app.run(debug=True, port=4000, host="0.0.0.0")