FROM python:3.7-slim

WORKDIR .

COPY requirements.txt requirements.txt

RUN apk add --no-cache gcc musl-dev linux-headers libc-dev

RUN pip install -r requirements.txt

EXPOSE 5005

COPY . .

CMD ["python", "location_grpc_server.py"]
