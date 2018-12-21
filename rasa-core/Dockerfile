FROM python:2.7

RUN pip install --no-cache-dir rasa_core==0.10.3

COPY . .

ENTRYPOINT ["sh", "./entrypoint.sh"]
