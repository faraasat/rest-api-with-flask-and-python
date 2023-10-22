FROM python:3.12-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

VOLUME [ "/data" ]

COPY . .

EXPOSE 5000

CMD ["flask", "run", "--host", "0.0.0.0"]

# docker run -dp 5005:500 -w /app -v "$(pwd):/app" <name>