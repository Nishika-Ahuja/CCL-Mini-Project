FROM python:3.10.0-alpine3.15
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py .
EXPOSE 5001
CMD ["python", "app.py"]
