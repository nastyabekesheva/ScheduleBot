FROM python:3.8-slim
WORKDIR /src
RUN --mount=type=secret,id=github_token \
  cat /run/secrets/github_token
RUN apt update && apt install -y gcc 
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD python bot.py
