@echo off

start cmd /k ^
    "pip install pandas flask flask-cors" ^
    "& exit"
start cmd /k ^
    "cd frontend" ^
    "& npm install @angular/cli" ^
    "& npm install" ^
    "& npm audit fix" ^
    "& exit"