from functools import lru_cache
import logging
import json

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s:%(levelname)s: %(message)s")


@lru_cache(maxsize=None)
def load_standard_score_15():
    try:
        with open('standard_score/15_min.json') as f:
            standard_score = json.loads(f.read())
        logging.info('Successfully loaded 15_min.json')
        return standard_score
    except FileNotFoundError:
        logging.error('Critical: 15_min.json not found')


@lru_cache(maxsize=None)
def load_standard_score_20():
    try:
        with open('standard_score/20_min.json') as f:
            standard_score = json.loads(f.read())
        logging.info('Successfully loaded 20_min.json')
        return standard_score
    except FileNotFoundError:
        logging.error('Critical: 20_min.json not found')
