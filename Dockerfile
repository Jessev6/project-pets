FROM python:3.7-alpine

WORKDIR /usr/src

ADD requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT [ "uvicorn", "--host", "0.0.0.0", "--port", "80", "app.main:app" ]

HEALTHCHECK \
  --interval=5s \
  --timeout=1s \
  --retries=5 \
  CMD wget http://localhost/api/healthz -q -O - > /dev/null 2>&1
