# ambiente
python -m venv .pyenv
.\.pyenv\Scripts\activate


# flask
set FLASK_APP=app.py
set FLASK_ENV=development
flask run
python -m flask run