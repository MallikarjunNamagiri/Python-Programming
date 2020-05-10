FROM tiangolo/uwsgi-nginx-flask:python3.6

WORKDIR /app

COPY . /app

# We copy just the requirements.txt first to leverage Docker cache
RUN pip --no-cache-dir install -r requirements.txt

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD [ "Flaskblog.py" ]