############################################################
# Purpose	: Dockerize Django App to be used in AWS EC2
# Django	: 1.8.1
# OS		: Ubuntu 14.04
# WebServer	: nginx
# Database	: Postgres inside RDS
# Python	: 2.7
# VERSION	: 0.1
############################################################

# take base image from dockerhub
from ubuntu:14.04

maintainer Kim Stacks, kimcity@gmail.com

## telling Ubuntu there is no terminal
ENV DEBIAN_FRONTEND noninteractive

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

## for weasyprint
RUN apt-get install python-lxml libcairo2 libpango1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info --force-yes -y

## postgres dev symbols
RUN apt-get install -y libpq-dev

# install nginx
run apt-get install \
        nginx \
        --force-yes -y

# install supervisor via apt-get because pip cannot work
RUN apt-get install -y supervisor

########################################
## Install Django 
## and associated python modules
########################################

# Install pip
RUN easy_install pip

# Add and install Python modules
ADD requirements.txt /src/requirements.txt
RUN cd /src; pip install -r requirements.txt


# Bundle app source 
# so the folder ./djangoapp inside the host 
# gets copied into /src inide the container
ADD ./djangoapp /src

########################################
## Config files here!
########################################
## run nginx in daemon mode
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

## remove default nginx config
RUN rm /etc/nginx/sites-enabled/default

## symlink the config file so easier to modify
RUN ln -s /src/../nginx_configuration/django-app.conf	/etc/nginx/sites-enabled/

## symlink supervisor config file
RUN ln -s /src/../supervisord_configuration/supervisord.conf /etc/supervisor/conf.d/

# give ownership of /src to www-data
RUN chown -R www-data:www-data /src

# Expose container port to host
EXPOSE 80

# supervisord == python program
# used to keep linux packages or commands running

 
########################################
## Remove any unwanted packages
########################################
run apt-get autoremove --force-yes -y


## default command when you startup
CMD ["supervisord", "-n"]