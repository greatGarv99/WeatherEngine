# WeatherEngine
Custom django-app for weatherScraping! 

Check out the live app by clicking [here!](https://weather-engine99.herokuapp.com)

## Initialization

- Clone the app.

- Move to the directory of the app.

- Initialize a virtual environment. --> `virtualenv venv`
> Install virtualenv by `pip3 install virtualenv` or `pip install virtualenv`

- Activate the virtual environment. --> `source venv/bin/activate`

- Now install all dependencies. --> `pip3 install -r requirements.txt`

- Make the migrations by --> `python3 manage.py migrate`

- Register yourself as the superuser --> `python3 manage.py createsuperuser` and fill all the required fields.

- Bravo! You can succesfully run the app now! --> `python3 manage.py runserver`

Now move to [localhost:8000](http://127.0.0.1:8000/) to view your app!
Also go to */admin* to view the search history.


## Credits
The data provider for this scraper is www.timeanddate.com
