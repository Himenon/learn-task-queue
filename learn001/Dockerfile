FROM python:3.6

RUN pip install redis

RUN mkdir -p /code
WORKDIR /code

COPY ./worker.py /code
CMD ["python", "/code/worker.py"]
