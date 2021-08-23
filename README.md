# Arisbd
Angular.JS and Django rest (API) framework using MML use management poject

## Setup

### Dependancies

- Python 3.8.5 
- Django 3.0
- Postgresql 13.2


The following steps will walk you thru installation on a Mac. Linux should be similar.
It's also possible to develop on a Windows machine, but I have not documented the steps.
If you've developed django apps on Windows, you should have little problem getting
up and running.



Assuming you've cloned the repository, open Terminal and `cd ~/your/path/to/arisbd`.

Create a python virtual environment:
```bash/zsh
virtualenv venv --python=python3.8
```

Activate it:

```bash/zsh
source venv/bin/activate
```

Then create `.env` file and paste code from the `.env-sample` file otherwise your server doesn't run.  

Install the python dependencies which includes Django and other libraries.

```
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python3 manage.py runserver # or
./manage.py runserver
```
