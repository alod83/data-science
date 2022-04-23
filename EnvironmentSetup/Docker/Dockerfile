FROM python:slim
WORKDIR /app_home
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "./app.py"]