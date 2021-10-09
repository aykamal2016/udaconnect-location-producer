FROM python:3.9

WORKDIR .

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5005

ENTRYPOINT ["python", "location_grpc_server.py"]

