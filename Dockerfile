FROM python:3.11.5-alpine

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt
ENTRYPOINT [ "uvicorn", "seo_helper.main:app", "--host", "0.0.0.0", "--port", "5000" ]
