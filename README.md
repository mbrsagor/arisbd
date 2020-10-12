# Arisbd
Angular.JS and Django rest (API) framework using MML use management poject

## Setup

### Dependancies

- Python 3.8.5 
- Django 3.0
- Mysql 8.0.19


The following steps will walk you thru installation on a Mac. Linux should be similar.
It's also possible to develop on a Windows machine, but I have not documented the steps.
If you've developed django apps on Windows, you should have little problem getting
up and running.



### Create Database

Create the database by running the following commands in a mysql shell.
First after installation mysql you may the command: example
mysql -u root -p1234

```
create database "arsbd";
```

Assuming you've cloned the repository, open Terminal and `cd ~/your/path/to/arisbd`.

Create a python virtual environment:

```bash/zsh
virtualenv venv --python=python3.8
```

Activate it:

```bash/zsh
source venv/bin/activate
```

Install the python dependancies which includes django and other libraries.

```
pip install -r requirements.txt

python3 manage.py runserver # or
./manage.py runserver
```
