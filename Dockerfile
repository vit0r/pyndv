FROM python:3.10-slim

ENV PYTHONWARNINGS=ignore
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ADD ./setup.py ./setup.py
ADD ./pyndv ./pyndv

RUN python setup.py install --user

ENTRYPOINT ["pyndv"]
