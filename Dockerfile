FROM python:3.10-bullseye
ENV PYTHONUNBUFFERED=1
RUN apt-get update && apt-get -y upgrade
RUN useradd --create-home appuser
WORKDIR /home/appuser
USER appuser
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
COPY bots/config.py /bots/
COPY bots/favretweet.py /bots/
COPY bots/followfollowers.py /bots/
COPY bots/start.sh /bots/
COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt

WORKDIR /bots
CMD [ "python", "favretweet.py" ]
