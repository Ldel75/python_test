FROM python:3.9

WORKDIR /application


COPY requirements.txt requirements.txt
COPY ./src .
RUN pip3 install -r requirements.txt


CMD [ "pyhon3", "app.py"]