### Notes: 

Running the app Using Gunicorn: `poetry run gunicorn -b 0.0.0.0:5000 -w 1 flask_app.app:app`

Running the integration tests: `poetry run python -m unittest discover -s tests`

Building the docker file: `sudo docker build -t my-flask-app .`

Running the app from the docker: `sudo docker run -p 5000:5000 my-flask-app` 
