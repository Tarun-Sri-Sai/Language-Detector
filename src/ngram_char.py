from os import path, system
from json import load, dump
from pandas import read_csv
from string import punctuation
from re import sub
from time import perf_counter
from math import log


def get_ngrams(text, n):
    text_strip = sub(f"[\n\t {punctuation}]+", "", text)
    result = {}
    for i in range(len(text_strip) - n + 1):
        ngram = text_strip[i: i + n]
        result[ngram] = result.get(ngram, 0) + 1

    return result


def compute_log_probs(ngrams):
    sum_value = sum(value for _, value in ngrams.items())
    return {key: log(value) - log(sum_value) for key, value in ngrams.items()}


def get_langs_and_ngrams_log_probs(n, csv_path):
    train_csv = read_csv(csv_path, encoding="utf-8").dropna()
    langs_list = train_csv["lang"].unique().tolist()
    lang_range = range(len(langs_list))
    lang_text_list = [" ".join(
        [sentence for sentence in train_csv[train_csv["lang"] == lang]["sentence"]]) for lang in langs_list]
    lang_ngrams_list = [get_ngrams(
        lang_text_list[i], n) for i in lang_range]
    return langs_list, [compute_log_probs(lang_ngrams_list[i]) for i in lang_range]


def get_log_prob(text_ngrams, lang_ngrams_log_probs):
    return sum(lang_ngrams_log_probs.get(ngram, log(1e-10)) for ngram in text_ngrams)


def predict(text):
    start_time = perf_counter()
    N = 3
    MAX_INPUT_CHARS = 1024
    cache_path = path.join("cache", "cache.json")
    if not path.isfile(cache_path):
        system(f"echo {{}} > {cache_path}")

    csv_path = path.join("data", "sentences.csv")
    if open(cache_path, "r", encoding="utf-8").read().strip() == "{}":
        langs_list, lang_ngrams_log_probs_list = get_langs_and_ngrams_log_probs(
            N, csv_path)
        cache = {
            "langs_list": langs_list,
            "lang_ngrams_log_probs_list": lang_ngrams_log_probs_list
        }
        dump(cache, open(cache_path, "w", encoding="utf-8"), indent=4)
    else:
        json_data = load(open(cache_path, "r", encoding="utf-8"))
        langs_list = json_data["langs_list"]
        lang_ngrams_log_probs_list = json_data["lang_ngrams_log_probs_list"]

    text = text[:MAX_INPUT_CHARS]
    text_ngrams = get_ngrams(text, N)
    log_prob_dist_list = [get_log_prob(
        text_ngrams, lang_ngrams_log_probs_list[i]) for i in range(len(langs_list))]
    result = langs_list[log_prob_dist_list.index(max(log_prob_dist_list))]
    end_time = perf_counter()
    print(f"Process finished in {end_time - start_time:.2f}s")
    return result.upper()
