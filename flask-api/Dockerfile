FROM python:3.12-alpine

WORKDIR /app

COPY requirements.txt .

# for development
# RUN pip install -r requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# VOLUME [ "/data" ]

COPY . .

# for development
# EXPOSE 5000

# for development
# CMD ["flask", "run", "--host", "0.0.0.0"]
CMD ["gunicorn", "--bind", "0.0.0.0:80", "app:create_app()"]

# -c "flask run means" don't run the cmd in file rather run this command
# docker run -dp 5005:500 -w /app -v "$(pwd):/app" <name> sh -c "flask run"