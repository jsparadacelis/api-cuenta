FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /api_cuenta
WORKDIR /api_cuenta
ADD . /api_cuenta/
RUN pip3 install -r requirements.txt
