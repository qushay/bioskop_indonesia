FROM ubuntu:latest
MAINTAINER Qushay Bagas "bagas.qushay@gmail.com"

RUN apt-get update
# Install pip & selenium
RUN apt-get install -y python python-pip wget
RUN pip install selenium
# Install Required Packages
RUN apt-get install -y build-essential chrpath libssl-dev libxft-dev
RUN apt-get install -y libfreetype6 libfreetype6-dev libfontconfig1 libfontconfig1-dev
# Install PhantomJS
RUN wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
RUN tar xvjf phantomjs-2.1.1-linux-x86_64.tar.bz2 -C /usr/local/share/
# create a soft link phantomjs binary file to systems bin dirctory
RUN ln -sf /usr/local/share/phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/bin
# Install flask
RUN pip install flask

ADD now.py /home/now.py
ADD soon.py /home/soon.py

WORKDIR /home