FROM python

LABEL image for dcim-api

WORKDIR /docker-flask

ADD . /docker-flask

RUN pip3 install -r requirements.txt

EXPOSE 5000
ENV FLASK_APP=api.py

RUN pip3 install pandas

CMD ["flask", "run", "-h", "0.0.0.0", "-p", "5001"]
