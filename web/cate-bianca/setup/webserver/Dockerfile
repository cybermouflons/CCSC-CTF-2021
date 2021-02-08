FROM php:8.0.3-apache

RUN docker-php-ext-install mysqli pdo pdo_mysql

# Set the working directory to /var/www/html/
WORKDIR /var/www/html

# Copy the current directory contents into the container
COPY ./ /var/www/
RUN mv /var/www/app/* /var/www/html/

# Change owner of web root
RUN chown -R www-data:www-data /var/www/
