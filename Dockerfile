FROM python:3.9-slim

ENV PYTHONWARNINGS=ignore
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ARG SUSERNAME=pyndv
ARG APP_DIR=/tmp/${SUSERNAME}

RUN adduser --system ${SUSERNAME}

RUN apt update && apt upgrade -y

RUN mkdir -p ${APP_DIR}

WORKDIR ${APP_DIR}

ADD ./setup.py ./setup.py
ADD ./pyndv ./pyndv

RUN python setup.py install

USER ${SUSERNAME}

ENTRYPOINT ["pyndv"]
