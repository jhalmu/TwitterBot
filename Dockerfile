FROM python:3.10-bullseye
RUN apt-get update && apt-get -y upgrade
#RUN pip install ez_setup
RUN useradd --create-home appuser
WORKDIR /home/appuser
USER appuser
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
COPY bots/config.py /bots/
COPY bots/favretweet.py /bots/
COPY bots/followfollowers.py /bots/
COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt

WORKDIR /bots
CMD python favretweet.py ; python followfollowers.py
