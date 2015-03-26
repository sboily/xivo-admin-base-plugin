from python:2.7
MAINTAINER Sylvain Boily "sboily@avencall.com"

RUN apt-get -yq update \
   && apt-get -yqq dist-upgrade \
    && apt-get -yq autoremove

ADD . /usr/src/xivo-admin-base-plugin
WORKDIR /usr/src/xivo-admin-base-plugin
RUN pip install -r requirements.txt
RUN python setup.py install

EXPOSE 80

CMD xivo-admin
