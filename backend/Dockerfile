FROM python:3.11-buster

WORKDIR /usr/src/lct_app

ADD ./requirements.txt ./
RUN pip install -r ./requirements.txt

COPY . /usr/src/lct_app/

CMD python -m uvicorn main:app --host 0.0.0.0 --port 8085 --workers 4
