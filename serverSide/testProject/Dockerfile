FROM python:3.11.3

WORKDIR /app

COPY . /app

RUN apt install -y curl && pip install Django

CMD ["python", "manage.py", "runserver", "0:8000"]
