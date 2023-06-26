FROM python:3.8

WORKDIR /fonetika

EXPOSE 33

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./fonetika.py" ]
