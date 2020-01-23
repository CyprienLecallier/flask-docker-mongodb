FROM python:3.6.8
ENV http_proxy http://proxy-essi.reseau.ratp:3128/
ENV https_proxy http://proxy-essi.reseau.ratp:3128/
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
