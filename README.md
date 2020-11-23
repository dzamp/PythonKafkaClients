##PYTHON CLIENTS SETUP AND CONFIGURATION
This project has been tested with python3.8 in a virtual environment. 
Extract the clients.zip on your preferred directory.
Create a virtualenv in the extracted ARESIBO folder. 


### VIRTUALENV setup 
``` 
$pwd
/home/<user>/ARESIBO
$ python3.8 -m venv PythonClients 
$ mv PythonAvroProducerConsumer/ PythonClients/
$ cd PythonClients 
$ source bin/activate
``` 
Verify we are running the correct python (python3.8)
```
(PythonClients)$ python 
```
Expected output: 
```
Python 3.8.3 (default, May 14 2020, 22:09:32) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```
Install the requirements:
```
(PythonClients)$ pip install -r requirements.txt 
```









