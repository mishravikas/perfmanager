#! /bin/bash

# Hack to wait for db to be up and running
sleep 10

python /srv/www/perfmanager/manage.py migrate

python /srv/www/perfmanager/manage.py loaddata /srv/www/perfmanager/initial_data.json

echo "Starting Server"

python /srv/www/perfmanager/manage.py runserver 0.0.0.0:8000
