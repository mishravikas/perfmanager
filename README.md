#perfmanager
Mozilla perfomance alerts manager

##Ubuntu 14.04 Development Build Instructions

1. Visit [Docker][docker] and get docker up and running on  your system.

2. Add your user to the `docker` system group. You may need to start a new terminal/session after doing this. Check the output of ``docker ps`` and if you don't see permissions warnings you should be fine.

3. Install docker-compose by following the instructions on [this page][docker-compose]

4. Run the following git clone (specify a directory of your choosing if you like):

        git clone https://github.com/mishravikas/perfmanager.git

5. cd into the name of the directory into which you cloned the git repository

        cd perfmanager

6. Run virtualenv on the git cloned directory to setup the Python virtual environment:

        virtualenv venv

7. Activate the virtual environment:

        source venv/bin/activate

8. Run docker-compose to set up the environment:

        docker-compose -f dockerfiles/docker-compose.yml up --no-recreate

9. On first run, run migrations and load initial data

        docker exec $(docker-compose -f dockerfiles/docker-compose.yml ps -q web) python /srv/www/perfmanager/manage.py migrate
        docker exec $(docker-compose -f dockerfiles/docker-compose.yml ps -q web) python /srv/www/perfmanager/manage.py loaddata /srv/www/perfmanager/initial_data.json

10. Visit [http://localhost:8080/][localhost] in your browser once you see `Starting Server` on the console. Press Ctrl-C on the console to stop the containers

11. Henceforth, use `docker-compose -f dockerfiles/docker-compose.yml up --no-recreate` to restart the containers.

[docker]: https://docs.docker.com/installation/
[docker-compose]: http://docs.docker.com/compose/install/
[localhost]: http://localhost:8080

###Executing commands on running containers

Until docker-compose [issue #593][issue-593] is resolved, please use the following syntax to run commands on the web service

        docker exec $(docker-compose -f dockerfiles/docker-compose.yml ps -q web) <COMMAND>

For example, refer to point 9 above for running migrations and loading initial data on first run.

[issue-593]: https://github.com/docker/compose/issues/593
