FROM python:3.9-slim

RUN apt update && apt upgrade -y

ENV PYTHONWARNINGS=ignore
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ARG SUSERNAME=pyndv

ARG APP_DIR=/home/${SUSERNAME}

RUN adduser -q ${SUSERNAME} --home ${APP_DIR}

WORKDIR ${APP_DIR}

ADD ./setup.py ./setup.py

ADD ./pyndv ./pyndv

ENV PATH=${PATH}:${APP_DIR}/.local/bin:${APP_DIR}/.local/lib/python3.9/site-packages

USER ${SUSERNAME}

RUN python setup.py install --user

CMD ["pyndv"]
