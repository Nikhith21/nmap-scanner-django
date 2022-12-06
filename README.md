# nmap-scanner-django

Installation
In order to use the nmap Python library, Nmap has to be installed on your system, if you don't have Nmap installed on your system, you can find a guide here
Create a virtual enviroment for the django dependencies Link official documentation

Activate the enviroment and go to the nmap-scanner-django folder and install the Django dependencies with the following command using the requirements.txt file which has the dependencies

pip install -r requirements.txt

To create the the database and tables, on the nmap-scanner-django folder run the following commands (python or python3 depends on your configuration when the enviroment variable on the system was set up)

python manage.py makemigrations

python manage.py migrate

Running
Go to the nmap-scanner-django folder and run

python manage.py runserver

The url where the form to perform the scan is located is: network-scanner ,so the url would be http://127.0.0.1:8000/network-scanner/
