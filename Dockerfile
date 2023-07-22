FROM python:3.9
ENV PYTHONUNBUFFERED 1
RUN apt-get -y update && apt-get -y upgrade
WORKDIR /usr/src/app/
COPY . /usr/src/app/
RUN chmod +x /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/wait-for-it.sh
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]