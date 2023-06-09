FROM python:3.10.6

COPY . /app

WORKDIR /app

RUN pip3 install -r requirements.txt
CMD ["python3", "main.py"]



