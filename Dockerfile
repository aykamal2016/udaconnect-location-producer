FROM python:3.9

WORKDIR .

RUN apk add --no-cache gcc musl-dev linux-headers libc-dev

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

EXPOSE 5005

COPY . .

CMD ["python", "location_grpc_server.py"]
