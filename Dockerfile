FROM ubuntu:16.04
LABEL maintainer "Youngseok Lee<lee@cnu.ac.kr>"
LABEL "purpose"="practice"
RUN apt-get update

COPY . /usr/src/app
WORKDIR /usr/src/app

EXPOSE 6789
CMD ["python3", "WebServer.py"]
