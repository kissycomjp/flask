FROM ubuntu:latest
RUN apt-get update
RUN apt-get install python3 python3-pip -y
RUN pip3 install flask
copy app.py home/app.py
CMD ["/usr/bin/python3", "/home/app.py"]
