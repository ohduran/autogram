FROM python:3.7-slim-stretch
WORKDIR /code
RUN apt-get update \
    && apt-get install -y --no-install-recommends --no-install-suggests \
    wget \
    gcc \
    g++ \
    chromedriver

COPY ./requirements /requirements
RUN pip install -r /requirements/instapy.txt

RUN apt-get purge -y --auto-remove \
    gcc \
    g++ \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/requirements.txt

CMD ["./compose/production/instapy/entrypoint.sh", "http://selenium:4444/wd/hub", "python", "insta.py"]
