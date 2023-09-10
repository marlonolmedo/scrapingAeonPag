FROM python

RUN mkdir -m 777 /codes

RUN pip install requests \
    && pip install BeautifulSoup4

EXPOSE 80 8080