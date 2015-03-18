#! /bin/bash

# Hack to wait for db to be up and running - to be removed when
# docker-compose issue #374 is resolved
sleep 15

echo "Starting Server"

python /srv/www/perfmanager/manage.py runserver 0.0.0.0:8000
