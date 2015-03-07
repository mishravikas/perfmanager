FROM ubuntu

MAINTAINER Gaurav Narula <gnarula94@gmail.com>

VOLUME /srv/www/perfmanager

# Don't prompt for any info
ENV DEBIAN_FRONTEND noninteractive

# Update
RUN apt-get -q -y update && apt-get -q -y upgrade

# Install dependencies
RUN apt-get -q -y install libmysqlclient-dev python-pip git curl python-dev mysql-client
RUN mkdir -p /srv/www/perfmanager

# Install python dependencies
ADD requirements.txt /tmp/requirements.txt
RUN ["/usr/bin/pip", "install", "-r", "/tmp/requirements.txt"]
RUN ["/bin/rm", "/tmp/requirements.txt"]

# Unset DEBIAN_FRONTEND
ENV DEBIAN_FRONTEND ''

# Run the development server
CMD /bin/bash /srv/www/perfmanager/run.sh
