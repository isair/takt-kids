KONTAKT Information Distribution System
=========
# Introduction
KIDS is the web based system which handles the ticket sales, achievement tracking, cosplay contest management, and many more aspects of the biggest subculture event (as of this writing) in Turkey.

# Setup
After cloning this repo, you need to set the following environment variables on your local machine:

* AWS_ACCESS_KEY_ID
* AWS_SECRET_ACCESS_KEY

These variables are your amazon web services access key id and secret access key respectively as their names suggest. After setting them, change the **AWS_STORAGE_BUCKET_NAME** variable in *settings.py* to the name of your own bucket then run a *collectstatic* command like this in the project directory:

```
python manage.py collectstatic
```

You should also install the required python packages using:

```
pip install -r requirements.txt
```

Installing them in a virtual environment is recommended but not required. Finally, you can run the server on your local machine with the following command:

```
python manage.py runserver 0.0.0.0:8000
```