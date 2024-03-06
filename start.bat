@echo off

git pull origin master

call .venv\Scripts\activate.bat

ECHO instaling requirements

pip install -r requirements.txt

python main.py

ECHO programm finished 
ECHO check output folder for finished product

PAUSE