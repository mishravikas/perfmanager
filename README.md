#perfmanager
Mozilla perfomance alerts manager

##Ubuntu 14.04 Development Build Instructions

1. Visit [Docker][docker] and get docker up and running on  your system.

2. Add your user to the `docker` system group. You may need to start a new terminal/session after doing this. Check the output of ``docker ps`` and if you don't see permissions warnings you should be fine.

3. Install docker-compose by following the instructions on [this page][docker-compose]

3. Run the following git clone (specify a directory of your choosing if you like):

        git clone https://github.com/mishravikas/perfmanager.git

4. cd into the name of the directory into which you cloned the git repository

        cd perfmanager

5. Run virtualenv on the git cloned directory to setup the Python virtual environment:

        virtualenv venv

6. Activate the virtual environment:

        source venv/bin/activate

7. Run docker-compose to set up the environment:

        cd dockerfiles; docker-compose up --no-recreate

8. Visit [http://localhost:8080/][localhost] in your browser once you see `Starting Server` on the console.

[docker]: https://docs.docker.com/installation/
[docker-compose]: http://docs.docker.com/compose/install/
[localhost]: http://localhost:8080
