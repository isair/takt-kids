[![Stories in Ready](https://badge.waffle.io/isair/takt-kids.png?label=ready&title=Ready)](https://waffle.io/isair/takt-kids)
Introduction
--------------
[![Gitter](https://badges.gitter.im/Join Chat.svg)](https://gitter.im/isair/takt-kids?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

K.I.D.S. is the web based system which handles the ticket sales, achievement tracking, cosplay contest management, and many more aspects of the biggest subculture event (as of this writing) in Turkey. It stands for __KONTAKT Information Distribution System__.

Quick Start
--------------

If you have a Mac yet don't have [Homebrew](http://brew.sh) installed, go ahead and install that on your system first. It will make the installation of any missing requirements way easier.

Requirements:
* Python 2.7 (On Mac: _brew install python_)
* PostgreSQL (On Mac: _brew install postgresql_)
* virtualenv (_pip install virtualenv_)

Make sure you have all the requirements installed on your machine, then clone this repository. Next, open a terminal and cd into the project directory. Enter the following lines in their given order.

```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8000
```

Congratulations! You now have a K.I.D.S. server running on your local machine! To stop the server just press __CTRL-C__.
