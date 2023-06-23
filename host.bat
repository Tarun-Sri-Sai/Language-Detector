@echo off

start cmd /k "cd server & python src/server.py"
start cmd /k "cd language-detector & ng serve"