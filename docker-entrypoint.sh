#!/bin/sh

flask db init
flask db migrate
flask db upgrade

cd /app
exec python3 app.py