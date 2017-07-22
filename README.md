# Steel-Kiwi-test

#### Install python environment
---------------------------------
python3.5 -m venv <venv name>

#### Project configuration process
---------------------------------
#### Commands for creating a database (postgres)
sudo -u postgres psql
CREATE DATABASE test_database;
CREATE USER test_user WITH password 'qwerty'; GRANT ALL ON DATABASE test_database TO test_user;
ALTER USER django CREATEDB;

#### Install dependencies
--------------------------------
pip install -r requirements.txt

#### Execute migrations (migrations will create default data and django superuser)
python manage.py migrate

#### Follow this link http://127.0.0.1:8000/products/
