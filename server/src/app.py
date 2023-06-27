import os
import json
import pandas as pd
import string
import re
import math


class App:
    def __init__(self):
        self.N = 3
        self.MAX_INPUT_CHARS = 1024

        self.cache_path = os.path.join('..', 'cache', 'cache.json')
        self.csv_path = os.path.join('..', 'data', 'sentences.csv')

        if not os.path.isfile(self.cache_path):
            os.system(f'echo {{}} > {self.cache_path}')

        if open(self.cache_path, 'r', encoding='utf-8').read().strip() == '{}':
            (self.langs_list,
             self.lang_ngrams_log_probs_list) = self.get_langs_and_ngrams_log_probs(
                self.N, self.csv_path)

            cache = {
                'langs_list': self.langs_list,
                'lang_ngrams_log_probs_list': self.lang_ngrams_log_probs_list
            }
            print(f'Writing cache to {self.cache_path}')
            json.dump(
                cache, open(self.cache_path, 'w', encoding='utf-8'), indent=4)
        else:
            print(f'Reading cache from {self.cache_path}')
            json_data = json.load(open(self.cache_path, 'r', encoding='utf-8'))

            self.langs_list = json_data['langs_list']
            self.lang_ngrams_log_probs_list = json_data['lang_ngrams_log_probs_list']

    def detect(self, text):
        text = text[:self.MAX_INPUT_CHARS]

        text_ngrams = self.get_ngrams(text, self.N)

        log_prob_dist_list = [self.get_log_prob(text_ngrams, self.lang_ngrams_log_probs_list[i])
                              for i in range(len(self.langs_list))]

        result = self.langs_list[log_prob_dist_list.index(
            max(log_prob_dist_list))]
        return result.upper()

    def get_ngrams(self, text, n):
        text_strip = re.sub(f'[\n\t {string.punctuation}]+', '', text)
        result = {}
        for i in range(len(text_strip) - n + 1):
            ngram = text_strip[i: i + n]
            result[ngram] = result.get(ngram, 0) + 1

        return result

    def compute_log_probs(self, ngrams):
        sum_value = sum(value for _, value in ngrams.items())
        return {
            key: math.log(value) - math.log(sum_value)
            for key, value in ngrams.items()
        }

    def get_langs_and_ngrams_log_probs(self, n, csv_path):
        train_csv = pd.read_csv(csv_path, encoding='utf-8').dropna()
        langs_list = train_csv['lang'].unique().tolist()
        lang_range = range(len(langs_list))

        lang_text_list = [' '.join(
            [sentence for sentence in train_csv[train_csv['lang'] == lang]['sentence']])
            for lang in langs_list]
        lang_ngrams_list = [self.get_ngrams(lang_text_list[i], n)
                            for i in lang_range]
        return langs_list, [self.compute_log_probs(lang_ngrams_list[i])
                            for i in lang_range]

    def get_log_prob(self, text_ngrams, lang_ngrams_log_probs):
        return sum(
            lang_ngrams_log_probs.get(ngram, math.log(1e-10))
            for ngram in text_ngrams)
