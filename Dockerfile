FROM python:2.7
MAINTAINER Muhammad Hassan "muhammad.hassan.102@gmail.com"

COPY . /usr/src/app
WORKDIR /usr/src/app

RUN pip install -r requirements.txt
RUN git clone https://github.com/iRB-Lab/py-ga-VRPTW.git

CMD ["python", "app.py"]

