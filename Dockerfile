FROM docker.io/ykang/centos7_basic:latest

RUN yum update -y \  
    && yum install -y epel-release \
    && yum install -y python2-pip \
    && pip install --upgrade pip \
    && pip install gunicorn \
    && pip install falcon \
    && pip install requests

ENV VERSION v0.0.1

WORKDIR /oakridge
