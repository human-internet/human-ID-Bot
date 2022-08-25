#!/bin/sh
#gunicorn --chdir app app:app - 
#w 2 --threads 2 -b 0.0.0.0:80
gunicorn -w 4 -b 18.225.5.208:8000 'app:index'
