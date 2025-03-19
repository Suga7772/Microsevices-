FROM python:3.9-slim

# Install SQLite3 (required for the database)
RUN apt-get update && apt-get install -y sqlite3

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

# Initialize the database (if needed)
RUN if [ -f "init_db.sql" ]; then sqlite3 notes.db < init_db.sql; fi

EXPOSE 8000
CMD ["python", "app/main.py"]