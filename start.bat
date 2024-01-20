@echo off

git pull origin master

call venv\Scripts\activate.bat

pip install -r requirements.txt

python main.py

PAUSE