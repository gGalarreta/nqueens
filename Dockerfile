FROM python:3.8-alpine

RUN apk update && \
    apk add --no-cache --virtual build-deps gcc python3-dev musl-dev && \
    apk add postgresql-dev

WORKDIR /app

ENV FLASK_APP app.py

COPY . /app

RUN pip --no-cache-dir install -r requirements.txt

# DB migrations
RUN chmod +x app.py

# Make Entrypoint executable
RUN chmod +x /app/docker-entrypoint.sh

# CMD ["python3", "app.py"]
CMD ["/bin/sh", "/app/docker-entrypoint.sh"]