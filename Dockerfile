FROM python:3
ENV PYTHONBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN sudo apt-get install libmysqlclient-dev
RUN pip install -r requirements.txt
ADD . /code/