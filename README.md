# Language Detector

## About

Language Detector is an application that can detect the language of a text across 135 languages. It only requires 20 characters to accurately detect 90% of text from the language if it maintains proper punctuation and grammar.

## Getting Started

### Prerequisites

- Requires an installation of [Python 3](https://python.org/downloads).
- Requires an installation of [Node.js](https://nodejs.org/en/download/current) package that includes NPM package manager.

### Setup

- Repository can be forked using:

    ```bash
    git fork https://github.com/Tarun-Sri-Sai/Language-Detector.git
    ```

- For Windows, navigating to the repository in Command Prompt and running the following command will finish setup:

    ```bash
    setup
    ```

## Usage

- For Windows, navigating to the repository in Command Prompt and running the following command will launch a test version of the application at <localhost:4200>:

    ```bash
    launch
    ```

- The application automatically detects when valid number of characters have been entered in a period of 0.5 sec.

## Inside the application

- The application uses Angular.JS, Bootstrap CSS, Python Flask and Pandas libraries.
- The language detection is done by using a `4-gram character` model with `log probabilities` which lets the model record probabilities of the order `10^-15` or smaller.
- The `data_13k.csv` consists `1,000-13,000` sentences in each language for upto `135` languages, which is accessed using Pandas library.
