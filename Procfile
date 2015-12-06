web: gunicorn superpunch.wsgi -c etc/config/gunicorn.py
worker: celery --workdir=superpunch/ --app=superpunch.celery:app worker
beat: celery --workdir=superpunch/ --app=superpunch.celery:app beat
flower: celery --workdir=superpunch/ --app=superpunch.celery:app flower
