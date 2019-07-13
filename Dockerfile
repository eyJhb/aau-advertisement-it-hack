FROM python:slim

# RUN apt-get update && \
#     apt-get install -y python-flask python3-flask
RUN pip install flask && pip3 install flask
RUN echo "TUFLRSBJVCBSRUFMIC0gTEFFUyBDT01QVVRFUlRFS05PTE9HSSBQQUEgQUFVIE9HIEFSQkVKRCBNRUQgQ1lCRVJTSUtLRVJIRUQ=" >> /tmp/flag.txt
RUN usermod --password ITC root
WORKDIR /src

# RUN python flask.py
