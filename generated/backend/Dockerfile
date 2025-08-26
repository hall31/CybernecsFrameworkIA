FROM php:8.2-cli
RUN apt-get update && apt-get install -y unzip git curl libpq-dev \
  && docker-php-ext-install pdo pdo_pgsql
WORKDIR /app
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
RUN composer create-project laravel/laravel .
CMD ["php", "artisan", "serve", "--host=0.0.0.0", "--port=9000"]
