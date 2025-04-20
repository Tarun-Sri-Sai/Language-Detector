from os import path, mkdir, system
from json import load, dump
from pandas import read_csv
from re import sub
from math import log
from string import punctuation


class Language:
    def __init__(self):
        self.N = 3
        self.MAX_INPUT_CHARS = 1024

        self.cache_dir = path.join('data', 'cache')
        if not path.isdir(self.cache_dir):
            mkdir(self.cache_dir)

        self.cache_path = path.join(self.cache_dir, 'cache.json')
        if not path.isfile(self.cache_path):
            system(f'echo {{}} > {self.cache_path}')

        self.csv_dir = path.join('data')
        self.csv_path = path.join(self.csv_dir, 'lang_13k.csv')
        if open(self.cache_path, 'r', encoding='utf-8').read().strip() == '{}':
            self.write_to_cache()
        else:
            self.read_from_cache()

    def write_to_cache(self):
        self.csv_data = self.get_csv_data()
        self.langs_list = self.get_langs()
        self.lang_ngrams_log_probs_list = self.get_lang_ngrams_log_probs()
        cache = {
            'langs_list': self.langs_list,
            'lang_ngrams_log_probs_list': self.lang_ngrams_log_probs_list
        }

        print(f'Writing cache to {self.cache_path}')
        with open(self.cache_path, 'w', encoding='utf-8') as cache_writer:
            dump(cache, cache_writer, indent=4)

    def read_from_cache(self):
        print(f'Reading cache from {self.cache_path}')
        with open(self.cache_path, 'r', encoding='utf-8') as cache_reader:
            json_data = load(cache_reader)

        self.langs_list = json_data['langs_list']
        self.lang_ngrams_log_probs_list = json_data['lang_ngrams_log_probs_list']

    def get_csv_data(self):
        return read_csv(self.csv_path, encoding='utf-8').dropna()

    def get_langs(self):
        return self.csv_data['lang'].unique().tolist()

    def get_ngrams(self, text, n):
        text_strip = sub(f'[\n\t {punctuation}]+', '', text)
        result = {}
        for i in range(len(text_strip) - n + 1):
            ngram = text_strip[i: i + n]
            result[ngram] = result.get(ngram, 0) + 1

        return result

    def compute_log_probs(self, ngrams):
        sum_value = sum(value for _, value in ngrams.items())
        return {key: log(value) - log(sum_value)
                for key, value in ngrams.items()}

    def get_lang_ngrams_log_probs(self):
        lang_range = range(len(self.langs_list))
        lang_text_list = [
            ' '.join([
                sentence
                for sentence in (self.csv_data[self.csv_data['lang'] == lang]
                                 ['sentence'])])
            for lang in self.langs_list
        ]

        lang_ngrams_list = [self.get_ngrams(lang_text_list[i], self.N)
                            for i in lang_range]

        return [self.compute_log_probs(lang_ngrams_list[i])
                for i in lang_range]

    def get_log_prob(self, text_ngrams, lang_ngrams_log_probs):
        return sum(lang_ngrams_log_probs.get(ngram, log(1e-10))
                   for ngram in text_ngrams)

    def compute_language(self, text):
        text = text[: self.MAX_INPUT_CHARS]
        text_ngrams = self.get_ngrams(text, self.N)
        log_prob_dist_list = [
            self.get_log_prob(text_ngrams,
                              self.lang_ngrams_log_probs_list[i])
            for i in range(len(self.langs_list))
        ]

        result = self.langs_list[log_prob_dist_list.index(
            max(log_prob_dist_list))]

        return result.upper()
