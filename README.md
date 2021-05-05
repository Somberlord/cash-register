# cash-register
Python web cash register software

Preparing venv
pip install flask flask-sqlalchemy flask-login

Using bulma
Download bulma sources in src/bulma folder
Then launch sass (gem install sass to install)
sass --watch --sourcemap=none sass/mystyles.scss:statics/css/style.css

Launchin app
Windows : 
set FLASK_ENV=development
set FLASK_APP=src
flask run