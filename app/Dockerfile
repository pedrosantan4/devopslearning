FROM python:3.10-slim
WORKDIR /app
COPY app/requirements.txt .
RUN pip install -r requirements.txt
COPY app/ .
CMD ["flask", "--app", "app.py", "run", "--host=0.0.0.0"]