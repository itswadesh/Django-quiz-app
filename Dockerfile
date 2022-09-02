
FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . . 
RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py createsuperuser


EXPOSE 8000


 


