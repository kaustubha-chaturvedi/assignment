FROM python:3.11-slim
RUN apt-get update && apt-get install -y apache2 apache2-utils libapache2-mod-wsgi-py3 && pip install virtualenv

ADD ./config.conf /etc/apache2/sites-available/000-default.conf
COPY ./app /var/www/app

WORKDIR /var/www/
RUN chown root:www-data app && chmod -R 777 app 
WORKDIR /var/www/app
RUN echo "DEBUG=False">.env
RUN mkdir error && virtualenv app && . app/bin/activate && pip install -r requirements.txt && python manage.py collectstatic --noinput && deactivate
RUN chmod -R 777 /var/www/app/db.sqlite3 && chmod -R 777 /var/www/app/core/ && chmod -R 777 /var/www/app/error
EXPOSE 80 
CMD ["apache2ctl", "-D", "FOREGROUND"]