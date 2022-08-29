FROM python:3.6.12-alpine
FROM gorialis/discord.py

COPY requirements.txt /
RUN pip3 install -r /requirements.txt
RUN pip3 install gunicorn Flask pyshorteners requests 
COPY . /app
WORKDIR /app
RUN chmod +x gunicorn.sh
USER root
RUN  ls /app
ENTRYPOINT ["/app/gunicorn.sh"]


#RUN mkdir -p /usr/src/bot
#WORKDIR /usr/src/bot
#COPY . .
#RUN apt-get update

#CMD [ "python3", "discordbot.py"]
