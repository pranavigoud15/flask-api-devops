FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install -r requirments.txt

CMD ["python", "app.py"] 