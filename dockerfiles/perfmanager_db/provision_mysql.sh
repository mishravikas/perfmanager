#!/bin/bash

# Set up perf_user and grant permissions to the database

DEBIAN_FRONTEND=noninteractive

# Fix permissions of /var/lib/mysql
mkdir -p -m 700 /var/lib/mysql
chown -R mysql:mysql /var/lib/mysql

# fix permissions and ownership of /run/mysqld
chown -R mysql:root /run/mysqld

# Initialize mysql data directory
mysql_install_db --user=mysql -ldata=/var/lib/mysql

dpkg-reconfigure --no mysql-server-5.5

/usr/sbin/service mysql start
printf "\033[1mSetting MySQL permissions\033[m\n"
mysql -u root -e "CREATE DATABASE IF NOT EXISTS perfdb;"
mysql -u root -e "GRANT ALL on perfdb.* to perf_user@'%';"
/usr/sbin/service mysql stop
exit
