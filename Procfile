# web: gunicorn mysite.wsgi --log-file -
web: waitress-serve --port=$PORT {mysite}.wsgi:application