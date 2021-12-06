FROM python:3.7.5-slim


#RUN apt update
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache numpy pandas joblib flask requests

WORKDIR /usr/src/app


COPY server_api.py ./
COPY bootstrap.sh ./


RUN chmod 755 /usr/src/app/server_api.py
RUN chmod +x /usr/src/app/server_api.py


# Start app

RUN chmod 755 /usr/src/app/bootstrap.sh
RUN chmod +x /usr/src/app/bootstrap.sh

EXPOSE 50021
ENTRYPOINT ["/usr/src/app/bootstrap.sh"]
