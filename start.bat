@echo off

start cmd /k ^
    "cd server" ^
    "& python server.py"

start cmd /k ^
    "cd language-detector" ^
    "& npm start"