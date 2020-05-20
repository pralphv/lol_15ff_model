from functools import lru_cache
import logging
import json

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s:%(levelname)s: %(message)s")


def _load_data(file_name: str):
    try:
        with open(f'standard_score/{file_name}') as f:
            standard_score = json.loads(f.read())
    except FileNotFoundError:
        with open(f'src/standard_score/{file_name}') as f:
            standard_score = json.loads(f.read())
    return standard_score


@lru_cache(maxsize=None)
def load_standard_score_15():
    try:
        standard_score = _load_data('15_min.json')
        logging.info('Successfully loaded 15_min.json')
        return standard_score
    except FileNotFoundError:
        error = 'Critical: 15_min.json not found'
        logging.error(error)
        raise FileNotFoundError(error)


@lru_cache(maxsize=None)
def load_standard_score_20():
    try:
        standard_score = _load_data('20_min.json')
        logging.info('Successfully loaded 20_min.json')
        return standard_score
    except FileNotFoundError:
        error = 'Critical: 20_min.json not found'
        logging.error(error)
        raise FileNotFoundError(error)
