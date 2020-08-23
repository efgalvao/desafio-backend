## Description:

This project is built on Python and Django Rest Framework, it provides a REST API for record, list, give a classification and a grade for the trips of the logged user.

It uses a SQLite database.


## Instalation instructions:

To run this project it's necessary to have python >= 3.5 installed and follow the steps below:

* Clone the github repository:
```
$ git clone https://github.com/efgalvao/desafio-backend.git
``` 

* Create a virtual environment:
```
$ python -m venv venv
```
* Activate it:
```
$ source ./venv/bin/activate
```
* Install the requirements:
```
$ pip install -r requirements.txt
```
* Create a .env file at the same folder of settings.py with the following entry:
```
SECRET_KEY=YourSecretKey
```
* Migrate the database:
```
$ python manage.py makemigrations
$ python manage.py migrate
```
* Run the server:
```
$ python manage.py runserver
```
# Endpoints:
```
/api/token/
    post:
      Authenticate with JWT.
/viagem/
    get:
      List all trips of the logged user
/viagem/{id}/:
    put:
      Update a trip
    patch:
      Partially update a trip
```
## Usage Instructions:
* To give a grade and/or give a choose a classification for a trip you need to send this payload (in json format) below:
```
{
  "id": 123,
  "data_inicio": "2020-02-20T12:10:00Z",
  "data_fim": "2020-02-20T12:20:00Z",
  "classificacao": 1,
  "nota": 3
}
```
