default: run

DATABASE_NAME=db.sqlite3


rebuild: deldb syncdb initdb

rebuild-win: deldb-win syncdb initdb

deldb-win:
	del -f $(DATABASE_NAME)

deldb:
	rm $(DATABASE_NAME)

syncdb:
	python manage.py migrate
	python manage.py makemigrations
	

initdb:
	sqlite3 $(DATABASE_NAME) < seed.sql

run:
	python manage.py runserver

