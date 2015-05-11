############################################################
# Purpose	: Dockerize Django App to be used in AWS EC2
# Django	: 1.8.1
# OS		: Ubuntu 14.04
# WebServer	: nginx
# Database	: Postgres inside RDS
# Python	: 2.7
# VERSION	: 0.1
############################################################

from ubuntu:14.04

maintainer Kim Stacks, kimcity@gmail.com

# make sure package repository is up to date
# this is commented out because it clashes with install build-essential
# run echo "deb http://archive.ubuntu.com/ubuntu trusty main universe" > /etc/apt/sources.list

run apt-get update

# run apt-get upgrade --force-yes -y

# install python
run apt-get install python	--force-yes -y				## install 2.7
run apt-get install python-setuptools --force-yes -y 	## for python2.7 or above
run apt-get install build-essential --force-yes -y 		##
run apt-get install python-virtualenv --force-yes -y 	## virtual env
run apt-get install python-dev --force-yes -y 		## because ubuntu 14.04 does not have dev version of python 2


# install nginx
run apt-get install \
        nginx \
        --force-yes -y
 
## copy the nginx config files
COPY ./nginx_configuration/common.conf 		/etc/nginx/common.conf
COPY ./nginx_configuration/fastcgi_params 	/etc/nginx/fastcgi_params
COPY ./nginx_configuration/nginx.conf 		/etc/nginx/nginx.conf
COPY ./nginx_configuration/php.conf 		/etc/nginx/php.conf
COPY ./nginx_configuration/default 			/etc/nginx/sites-available/default
COPY ./nginx_configuration/php.example 		/etc/nginx/sites-available/php.example

## copy the bash_rc over
# COPY ./bash_files/.bash_profile			/root/.bash_profile

run /etc/init.d/nginx restart
 
########################################
## Remove any unwanted packages
########################################
run apt-get autoremove --force-yes -y
