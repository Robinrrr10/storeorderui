FROM python:3.6-slim
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
RUN pip install --upgrade pip
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
ENV PRODUCT_HOST=http://localhost:8080  ORDER_MANAGEMENT_HOST=http://localhost:8080
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
