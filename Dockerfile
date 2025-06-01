FROM python:3.11

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["gunicorn", "-k", "eventlet", "-w", "1", "app:app", "-b", "0.0.0.0:5000"]
