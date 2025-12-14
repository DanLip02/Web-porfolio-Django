# Dockerfile
FROM python:3.11-slim

WORKDIR /portfolio_project

COPY requirements.txt /portfolio_project

RUN pip install --upgrade pip && \
    pip install -r requirements.txt --no-cache-dir

COPY . /portfolio_project

EXPOSE 8000

CMD ["python"]