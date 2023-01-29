FROM python:3-alpine3.10
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /dailyCheck/
RUN pip install -r requirements.txt
COPY . /app/
CMD ["python" "-m" "flask" "run" "--host=0.0.0.0"]
