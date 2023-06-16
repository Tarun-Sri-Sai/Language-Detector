import os
import json
import pandas as pd
import string
import re
import time
import math
import numpy as np


def get_ngrams(text, n):
    text_strip = re.sub(f'[\n\t {string.punctuation}]+', '', text)
    ngrams = [text_strip[i:i + n] for i in range(len(text_strip) - n + 1)]
    return np.array(ngrams)


def compute_log_probs(ngrams):
    unique_ngrams, counts = np.unique(ngrams, return_counts=True)
    sum_value = counts.sum()
    log_probs = np.log(counts) - np.log(sum_value)
    return {ngram: log_prob for ngram, log_prob in zip(unique_ngrams, log_probs)}


def get_langs_and_ngrams_log_probs(n, csv_path):
    train_csv = pd.read_csv(csv_path, encoding='utf-8').dropna()
    langs_list = train_csv['lang'].unique().tolist()
    lang_range = range(len(langs_list))
    lang_text_list = [' '.join([sentence for sentence in train_csv[train_csv['lang'] == lang]['sentence']]) for lang in langs_list]
    lang_ngrams_list = [get_ngrams(lang_text_list[i], n) for i in lang_range]
    lang_ngrams_log_probs_list = [compute_log_probs(ngrams) for ngrams in lang_ngrams_list]
    return langs_list, lang_ngrams_log_probs_list


def get_log_prob(text_ngrams, lang_ngrams_log_probs):
    return sum(lang_ngrams_log_probs.get(ngram, math.log(1e-10)) for ngram in text_ngrams)


def detect_language(text):
    start_time = time.perf_counter()
    N = 3
    MAX_INPUT_CHARS = 1024
    cache_path = os.path.join('cache', 'cache.json')
    if not os.path.isfile(cache_path):
        with open(cache_path, 'w', encoding='utf-8') as f:
            json.dump({}, f)

    csv_path = os.path.join('data', 'sentences.csv')
    with open(cache_path, 'r', encoding='utf-8') as f:
        cache = json.load(f)

    if not cache:
        langs_list, lang_ngrams_log_probs_list = get_langs_and_ngrams_log_probs(N, csv_path)
        cache = {
            'langs_list': langs_list,
            'lang_ngrams_log_probs_list': lang_ngrams_log_probs_list
        }
        with open(cache_path, 'w', encoding='utf-8') as f:
            json.dump(cache, f, indent=4)
        print(f'Writing cache to {cache_path}')
    else:
        print(f'Reading cache from {cache_path}')
        langs_list = cache['langs_list']
        lang_ngrams_log_probs_list = cache['lang_ngrams_log_probs_list']

    print(f'Processed {len(langs_list)} languages in {time.perf_counter() - start_time:.2f}s')

    text = text[:MAX_INPUT_CHARS]
    text_ngrams = get_ngrams(text, N)
    log_prob_dist_list = [get_log_prob(text_ngrams, lang_ngrams_log_probs_list[i]) for i in range(len(langs_list))]
    result = langs_list[np.argmax(log_prob_dist_list)]
    return result.upper()
