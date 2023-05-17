# wg-easy-logger
This is a course project for using docker. The aim is to create a logger for wg-easy server certificates.

Download Dockerfiles.

You can download WG-EASY from https://github.com/wg-easy/wg-easy
Use recommended installation, create account and issue a certificate.


CREATE VOLUME:
create a volume for project purposes by running:
docker volume create project_volume1


NGINX:
go to the /nginx dir and open a terminal. Type:
docker build -t nginx_docker -f Dockerfile .

run nginx:
docker run -p 8080:80 -v project_volume1:/var/www/html nginx_docker


FOR LOGGER:
Go to WG-EASY web UI (0.0.0.0:51821 unless changed) login with your password and grab the cookie. Place the cookie in the relevant field in logger.py (line 18) and save the file.

requirements.txt and logger.py should be in the same folder with Dockerfile. Open a terminal and run:
docker build -t wg_logger -f Dockerfile .

run the docker using the following command:
docker run -it -v project_volume1:/var/www/html --network=host wg_logger


activate a certificate issued by the wg-easy server.


Go to 127.0.0.1:8080 and watch the logging on the nginx webpage.
