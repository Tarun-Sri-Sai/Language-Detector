@echo off

start cmd /k "cd server/src & pip install pandas & pip install flask & pip install -U flask-cors & exit"
start cmd /k "cd language-detector & npm install & exit"