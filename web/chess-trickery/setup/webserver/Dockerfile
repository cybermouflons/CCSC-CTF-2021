# Use an official Python runtime as a parent image
FROM php:7.2-apache

# Set the working directory to /var/www/html/
WORKDIR /var/www/html

# Copy the current directory contents into the container
COPY ./ /var/www/
RUN mv /var/www/app/* /var/www/html/

# Change owner of web root
RUN chown -R www-data:www-data /var/www/

# Install sqlite3
RUN apt-get -y update
RUN apt-get install -y sqlite3 libsqlite3-dev
