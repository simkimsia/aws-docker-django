# aws-docker-django
Dockerized django setup on AWS


# steps to run boot2docker

1. RUN `boot2docker up`
2. RUN `boot2docker shellinit` #skip if environment settings already set
3. Copy paste and run the export lines #skip if environment settings already set
4. RUN `docker build -t <appname> .` # do this *once* after you make 
5. RUN `docker run --name <docker_instance_name> -d -p 80:80 <appname>`
6. RUN `boot2docker ip` #get the ip address

# steps to shut down the docker image
1. RUN `boot2docker down <appname>`
2. RUN `docker rm <docker_instance_name>`

# steps to shutdown the boot2docker
1. Shut down all running images
2. RUN `boot2docker down`

# how to see possible interactive 
`docker run --name <docker_instance_name> -i -p 80:80 <appname>`

# how to run docker image with environment variables
`docker run --name myez -d -p 80:80 -e PROD=True -e ALLOWED_HOST=127.0.0.1 ez`

# awsebcli
1. install awsebcli
2. eb init # this is only done once
3. eb create # this is only done once
4. # to redeploy from scratch, 
eb deploy # based on the folder u are running this in.
5. commit in the .elasticbeanstalk file folder into the github
6. eb open # shortcut to open browser