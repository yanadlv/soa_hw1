FROM python:3.9

RUN pip install netcat

COPY proxy.py .

CMD ["python3", "proxy.py"]