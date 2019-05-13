FROM ubuntu:16.04
FROM python:3
RUN mkdir -p uploads
COPY ./server.py /
COPY ./Kubernetes-76efc270ea69.json /
RUN export GOOGLE_APPLICATION_CREDENTIALS=/Kubernetes-76efc270ea69.json


RUN pip3 install virtualenv
RUN virtualenv venv
RUN /bin/bash -c "source ./venv/bin/activate"

RUN pip3 install flask
#RUN export GOOGLE_APPLICATION_CREDENTIALS=./Kubernetes-76efc270ea69.json
RUN pip3 install --upgrade google-api-python-client
RUN pip3 install google-cloud-speech

EXPOSE 5000

CMD ["python3","server.py"]
