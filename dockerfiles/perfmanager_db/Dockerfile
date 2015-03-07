FROM ubuntu

MAINTAINER Gaurav Narula <gnarula94@gmail.com>

# Don't prompt for info
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -q -y update && apt-get -q -y upgrade
RUN apt-get -q -y install mysql-common mysql-server supervisor

# Set up perf_user
COPY provision_mysql.sh /usr/local/bin/provision.sh
RUN chmod 755 /usr/local/bin/provision.sh
RUN /usr/local/bin/provision.sh

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
EXPOSE 3306

# Unset DEBIAN_FRONTEND
ENV DEBIAN_FRONTEND ''

CMD ["/usr/bin/supervisord"]
