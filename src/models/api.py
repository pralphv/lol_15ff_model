from joblib import load
import logging

from functools import lru_cache

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s:%(levelname)s: %(message)s')


@lru_cache(maxsize=None)
def load_15_model():
    logging.info('Loading 15 model')
    try:
        clf = load('models/15_min.joblib')
        logging.info('Successfully loaded 15_min.joblib')
        return clf
    except FileNotFoundError:
        # send email report
        error = 'Critical: 15_min.joblib not found'
        logging.error(error)
        raise FileNotFoundError(error)


@lru_cache(maxsize=None)
def load_20_model():
    logging.info('Loading 20 model')
    try:
        clf = load('models/20_min.joblib')
        logging.info('Successfully loaded 20_min.joblib')
        return clf
    except FileNotFoundError:
        # send email report
        error = 'Critical: 20_min.joblib not found'
        logging.error(error)
        raise FileNotFoundError(error)


def main():
    load_15_model()


if __name__ == '__main__':
    main()
