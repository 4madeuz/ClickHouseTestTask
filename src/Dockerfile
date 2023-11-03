FROM python:3.10

WORKDIR opt/app/src

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH '/opt/app'

COPY requirements.txt requirements.txt


RUN  pip install --upgrade pip \
     && pip install --no-cache-dir -r requirements.txt

COPY .. .

ENTRYPOINT ["python", "-m", "gunicorn", "-k", "uvicorn.workers.UvicornWorker", "src.services.main:app", "--bind", "0.0.0.0:8000"]
