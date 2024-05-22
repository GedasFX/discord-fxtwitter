FROM python:alpine

COPY . .

ENTRYPOINT [ "python", "./main.py" ]
