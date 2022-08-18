# search-smartly-test-project

**Table of Contents**

1. [Technologies](#technologies)
1. [Running Locally](#running-locally)
1. [Future Improvements](#future-improvements)

## Technologies

- Django 4.2
- Python 3.10
- Flake8


## Running Locally


### First Time Setup

1. Clone repo and cd into directory
1. Create virtual environment: `python -m venv venv` (you could also use Poetry for this step, but I think it's easier this way)
1. Run: `source venv/bin/activate`
1. Install packages: `pip install -r requirements.txt`
1. Run migrations: `python manage.py migrate`
1. Create an admin user for logging into the Django admin interface: `python manage.py createsuperuser`

### Running the App

1. Make sure you are already in your virtual environment: `source venv/bin/activate`
1. Run the app: `python manage.py runserver`
1. View the API at http://localhost:8000 and the admin interface at http://localhost:8000/admin

### Bash Command 

1. To add database from the files make sure to download files as pois.csv, pois.json and pois.xml
1. Run the script `python3 manage.py insert_data pois.json pois.csv pois.xml`

##  Future Improvements

1. We can add multithreading to this script which extract tons of data from these files.
1. As threading can reduce the time complexity.
1. We can make this project more efficient so that this can cater othertext files as well.