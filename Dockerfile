FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY static/ static/
COPY templates/ templates/
COPY stegano.py .

EXPOSE 80

CMD ["python", "stegano.py", "--host", "0.0.0.0", "--port", "80"]
