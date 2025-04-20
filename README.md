# Language Detector

## Description

A web application that takes in text and detects the language of the text. This will help if you need to know the language of a text that you don't seem to recognize or clearly distinguish. Using the dataset provided with this project, it can detect text among 135 languages.

## Requirements

This project requires the following software:

- docker: 28.0 or above
- 7z: 24 or above

## Usage

1. Extract `server/data.7z` into `server`.

   ```bash
   7z x "server/data.7z" -o"server"
   ```

2. Open Docker Desktop and run the following command in the terminal at the root of this repository:

   ```bash
   docker compose up --build
   ```

   To stop the container, run the following command:

   ```bash
   docker compose down
   ```
