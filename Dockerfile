#using the python image
FROM python:3

WORKDIR /app

COPY . /app

#installing dependencies require to run the application
RUN pip install -r requirements.txt

#setting the environment variable to use flask
ENV FLASK_APP=routes.py

#exposing port being used by flask
EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]
