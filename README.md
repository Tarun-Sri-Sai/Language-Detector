# Language-Recognizer

Language-Recognizer is a Python script `ngram_char_lang.py` that can detect the language of a given text. This repository contains the source code for this script along with two data files that the script uses for language recognition: `csv/sentences.csv` and `json/cache.json`.

## Usage

To use Language-Recognizer, you need to provide a text file that you want to detect the language of. The text file should be placed in the `txt` directory and should be named `input.txt`. The script will read the contents of this file and attempt to identify the language.

You can run the script using the following command:

```
python ngram_char_lang.py
```

Note that this script requires Python 3 to run.

## Data files

Language-Recognizer uses two data files to help with language recognition:

- `csv/sentences.csv`: This file contains example sentences for each language that the script can recognize. The script uses these sentences to calculate the frequencies of various character n-grams for each language.

- `json/cache.json`: This file stores the results of previous language detections. If the script has already detected the language of a given text, it will use the cached result instead of recalculating the frequencies of character n-grams for each language.

Note that both of these files are not included in the repository due to their large size. Instead, they are listed in the `.gitignore` file. If you want to use Language-Recognizer, you will need to provide your own versions of these files.