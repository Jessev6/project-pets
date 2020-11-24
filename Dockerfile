FROM python:3.7-alpine

WORKDIR /usr/src

ADD requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT [ "uvicorn", "--host", "0.0.0.0", "--port", "80", "app.main:app" ]
