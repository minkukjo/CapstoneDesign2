FROM ubuntu:16.04
FROM python:3

RUN apt-get update
RUN apt-get install -y portaudio19-dev
RUN pip3 install flask
RUN pip3 install requests

COPY ./sound_recorder.py /
COPY ./client.py /

CMD ["python3", "client.py"]
