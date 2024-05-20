FROM python:latest
WORKDIR /demo
RUN apt-get update -y \
    && apt-get upgrade -y 

COPY . .    
CMD [ "python","abc.py"]