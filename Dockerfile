FROM python:3.4

RUN mkdir -p /app/wsgi/static
RUN mkdir -p /app/wsgi/media

WORKDIR /app

VOLUME /app/wsgi/media
VOLUME /data

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY wsgi/application /app/wsgi/
COPY venelin /app/venelin
COPY manage.py /app/
COPY run /app/
RUN chmod +x /app/run

ENV DATA_DIR=/data
ENV DJANGO_ENV=docker

RUN python3 /app/manage.py collectstatic --noinput

EXPOSE 8000

CMD /app/run
