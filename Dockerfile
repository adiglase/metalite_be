FROM python:3.8 AS builder

ENV PYTHONUNBUFFERED=1
RUN apt-get update
RUN apt-get -y install build-essential default-libmysqlclient-dev 

# Create the virtual environment
RUN python3 -m venv /venv
ENV PATH=/venv/bin:$PATH

WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt


# Final stage
FROM python:3.8

COPY --from=builder /venv /venv
ENV PATH=/venv/bin:$PATH

COPY . /app/
WORKDIR /app
CMD python3 manage.py makemigrations && \
    python3 manage.py migrate && \
    python3 manage.py runserver 0.0.0.0:8000