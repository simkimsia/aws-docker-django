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
run echo "deb http://archive.ubuntu.com/ubuntu $(lsb_release -sc) main universe" > /etc/apt/sources.list

run apt-get update

# install python

# install nginx

