@echo off

start cmd /k ^
    "pip install pandas flask flask-cors" ^
    "& exit"
start cmd /k ^
    "cd language-detector" ^
    "& npm install @angular/cli" ^
    "& npm install" ^
    "& npm audit fix" ^
    "& exit"