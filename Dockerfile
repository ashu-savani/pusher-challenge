#using the python image 
FROM python:3

WORKDIR /app

COPY . /app

#installing dependencies require to run the application
RUN pip install -r requirements.txt

#setting the environment variable to use flask
ENV FLASK_APP=routes.py

CMD ["flask", "run"]