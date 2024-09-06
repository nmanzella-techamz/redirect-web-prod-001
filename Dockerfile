FROM python:3.12.4-alpine3.20

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

WORKDIR /code/app

EXPOSE 80/tcp

CMD ["fastapi", "run", "main.py", "--port", "80"]