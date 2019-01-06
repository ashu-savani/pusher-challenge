# pusher-challenge

## Challenge One 
To run the Flask server for challenge one, run the following commands
```
# create a virtual environment
python3 -m venv .
# install the requirements
pip install -r requirements.txt
# set an environment variable
export FLASK_APP=routes.py
#run the web server
flask run
```

## Challenge Two
The first step would be to build the docker image from the docker file
```
docker build -t pusher-challenge:latest
```
The next step would be to run the docker image
```
docker run -p 5000:5000 pusher-challenge
```
