FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY main.py .
COPY templates/ templates/
COPY static/ static/

EXPOSE 5000
CMD ["python", "main.py"]
