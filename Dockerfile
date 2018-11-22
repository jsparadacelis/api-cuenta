FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /api_cuenta
WORKDIR /api_cuenta
ADD . /api_cuenta/
RUN pip freeze > requirements.txt
RUN pip install -r requirements.txt
