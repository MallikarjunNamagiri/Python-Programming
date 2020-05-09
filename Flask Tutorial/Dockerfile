FROM tiangolo/uwsgi-nginx-flask:python3.6

COPY . /Flask_App

WORKDIR /Flask_App

# We copy just the requirements.txt first to leverage Docker cache
RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]

CMD [ "Flaskblog.py" ]