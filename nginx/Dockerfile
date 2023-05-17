#pull base image
FROM debian:latest

MAINTAINER JAn Wagner "waja@cyconet.org"

#Install nginx and adjust nginx config to stay in foreground
RUN apt-get update && apt-get install --no-install-recommends -y nginx; \
echo "daemon off;" >> /etc/nginx/nginx.conf

#EXPOSE HTTP
EXPOSE 80

#Start nginx
CMD ["/usr/sbin/nginx"]
