# 3DPrince

The point of this site is to simplify 3D printing for the end user to make it as simple as any other home applicance. By only allowing the best 3D printable models, a library can be built up that also enable slicing on demand.  The average user will need virtually no computer knowledge to benefit from 3D printing. A raspberry pi access this information through an API on the back end of the site, and displays it on the 3D printer at the users finger tips.<br>


After proving this concept on small scale, this current project is aimed at full deployment and actual production use. This is a site built around the demo-allauth-bootstrap template, which also uses [django-allauth](https://github.com/pennersr/django-allauth). There is a bit more work necessary before deployment, so the site now is focused on services instead of functionality. This currently has been tested and working on Linux and Windows.

Any help to this project would be greatly appreciated! Deployment is so close and from there this project can become self sustaining.

## tl;dr

This is is an opensource site built with Python on Django based around the idea of sharing 3D printer files (.stl and .ini) and allowing slicing to occuring from the server allows smaller computers (such as raspberry pis) to access gcode on command. 


## Installing

1. Download from the source.
2. Create a ``virtualenv`` and install requirements requirements : <br> <br>``pip install -r requirements.txt``<br>
<br> On Windows you must ensure ``sqlite3`` is installed and on your path and do the following command after the pip install.
<br>``easy_install Pillow``<br>
3. Start the server

## How to Start the server

1. From now on while your virtualenv is running, run ``python manage.py runservers`` to start the local server.

2. Visit http://127.0.0.1:8000/


This should get it started with a database attached. Allauth is the authentication and there are forms built up for the bootstrap3 front end.


## Login to site

To initialize a super user run ``python manage.py createsuperuser``. To create a local account, just use the login function on the website. 

## How to use virtualenv

Linux<br>
First run the following installation commands.<br>
``pip install virtualenv`` <br><br>
Create new virtualenv called "NewEnv". <br>
``virtualenv NewEnv`` <br><br>
Start the new new virtualenv. <br>
``source NewEnv/bin/activate`` <br><br>
Exit the virtualenv.<br>
``deactivate`` <br><br>

Windows<br>

First run the following installation commands.<br>
``pip install virtualenv virtualenvwrapper-win`` <br><br>
Create new virtualenv called "NewEnv". <br>
``mkvirtualenv NewEnv`` <br><br>
Start the new new virtualenv. <br>
``workon NewEnv`` <br><br>
Exit the virtualenv.<br>
``deactivate`` <br><br>


