FROM python:3.6

RUN mkdir /code
WORKDIR /code
COPY ./code /code
RUN pip install -r /code/requirements.txt

CMD ["python", "/code/server.py"]
