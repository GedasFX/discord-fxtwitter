FROM python:alpine

RUN pip install discord
COPY . .

ENTRYPOINT [ "python", "./main.py" ]
