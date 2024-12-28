FROM python:3.12-bullseye

ENV PYTHONUNBUFFERED=1

WORKDIR /ecommerce

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

# CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
