FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
ENV DATABASE_URL=postgresql://user:password@postgres-db:5432/mydb
EXPOSE 5000
CMD ["python", "app.py"]