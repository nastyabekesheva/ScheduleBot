FROM python:3.8-slim
WORKDIR /src
RUN apt update && apt install -y gcc 
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD python bot.py
