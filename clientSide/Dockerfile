FROM python:3.11.3

WORKDIR /clientApplication

COPY . /clientApplication/

RUN pip install requests

ENTRYPOINT [ "python", "client.py" ]