FROM python:2.7

COPY . .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r ./requirements.txt

ENTRYPOINT gunicorn --bind 0.0.0.0:8080 Dialog_Controller:app
