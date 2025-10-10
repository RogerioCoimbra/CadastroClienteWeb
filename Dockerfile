# Dockerfile
FROM php:8.4.10-cli-alpine
RUN docker-php-ext-install pdo pdo_mysql mysqli
WORKDIR /app
CMD ["php", "browse-users.php"]
