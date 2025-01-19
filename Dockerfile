FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["uvicorn", "--host", "0.0.0.0", "--port", "5000", "main:app"]