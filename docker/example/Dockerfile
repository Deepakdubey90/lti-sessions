FROM python:3-alpine

# add labels
LABEL author="akhilputhiry"
LABEL version="1.0.0"

# install artifacts
RUN mkdir /flask
COPY app.py /flask/app.py
COPY requirements.txt /flask/requirements.txt

# install dependencies
RUN pip install -r /flask/requirements.txt

# run app
ENTRYPOINT ["/usr/local/bin/python", "/flask/app.py"]

# expose port
EXPOSE 5000
