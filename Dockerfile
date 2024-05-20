FROM python:latest
WORKDIR /demo
RUN apt-get update -y \
    && apt-get upgrade -y 

COPY . .    
#i got an error at first (docker: Error response from daemon: failed to create task for container: failed to create shim task: OCI runtime create failed: runc create failed:
#unable to start container process: exec: "3": executable file not found in $PATH: unknown.ERRO[0000] error waiting for container:
#because i used "cmd"
ENTRYPOINT [ "python","abc.py"]
