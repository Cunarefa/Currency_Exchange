# CurrencyExchange

## Mac

Creating the environment:

```
make install
```

or

```
python3 -m venv venv  # create the python virtual environment
. venv/bin/activate  # activate the python virtual environment
pip install -r requirements.txt  # install our python dependencies
```

---

## Windows

Uninstall any previous installations of:
- Python
- PostgreSQL

Install Python 3.7.9 as Admin (https://www.python.org/downloads/release/python-379/)

Add both Python and Pip to Windows PATH Environment Variables
```
run sysdm.cpl
```

Creating the environment:
```
pip install virtualenv
virtualenv --python C:\Path\To\Python\python.exe venv
```

Installing dependencies:
```
. .\venv\Scripts\activate
pip install -r requirements.txt
```
---

## Environment variables:

- Create an `.env` file at the root of the project


## Dev DB Setup

1. Start the local database + redis server using Docker:

`docker-compose up`

2. Run migrations

```
docker-compose exec web python manage.py migrate --noinput
```

3. If get mistake: 
docker-compose exec web python manage.py migrate --noinput, Stop the container with command:
   
```
docker-compose down -v
```

Build images again, run containers and run migrations again

```
docker-compose up -d --build
docker-compose exec web python manage.py migrate --noinput
```
