FROM python:3.13-alpine3.21


ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN apk add --no-cache bash

WORKDIR /app

COPY ./backend/requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY ./backend .

RUN chmod +x ./run

CMD ["./run"]