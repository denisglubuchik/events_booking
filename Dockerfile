FROM python:3.10

RUN mkdir /events_booking

WORKDIR /events_booking

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x /events_booking/docker/*.sh

#CMD ["gunicorn", "app.main:app", "--workers", "4", "--worker-class", "uvicorn.worker.UvicornWorker", "--bind=0.0.0.0:8000"]

