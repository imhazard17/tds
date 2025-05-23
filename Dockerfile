FROM python:3

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

CMD [ "uvicorn", "api.main:app" ]
