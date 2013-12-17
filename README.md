# flask-paypal
=================================

Flask app for payment using python rest sdk

pip is the package manager for Python. Go to http://www.pip-installer.org/ if you do not have it yet.

    $ pip install virtualenv virtualenvwrapper

Afterwards follow instructions on http://virtualenvwrapper.readthedocs.org/ and create a virtualenv where we will work on. Let's call the environment flask-paypal.

Clone the repo

    (flask-paypal)$ git clone git@github.paypal.com:anadas/flask-paypal.git
    
Install requirements using pip

    (flask-paypal)$ pip install -r requirements.txt
    
Get your client credentials from https://developer.paypal.com/ and put them in a config file. Let's call it settings.cfg

    $ cat setttings.cfg
    MODE="sandbox"
    CLIENT_ID="EBWKjlELKMYqRNQ6sYvFo64FtaRLRR5BdHEESmha49TM"
    CLIENT_SECRET="EO422dn3gQLgDbuwqTjzrFgFtaRLRR5BdHEESmha49TM"
    
Export the configuration file for flask 

    $ export CONFIG="/path/to/settings.cfg"
    
Run the app!
    
    (flask-paypal)$ python app.py
    * Running on http://127.0.0.1:5000/
    * Restarting with reloader

Go to your browser and navigate to http://127.0.0.1:5000/