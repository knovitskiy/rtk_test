import requests
import logging
from constants import BODY_TOKEN, API_TOKEN_URL, API_MOVIES_URL, HEADER_TOKEN


logger = logging.getLogger()


def get_token(device_type):
    payload = BODY_TOKEN.copy()
    payload['device_type'] = device_type
    logger.info(f'Payload: {payload}')
    request = requests.post(url=API_TOKEN_URL, json=payload)
    logger.info(request.text)
    token = request.json()['token']
    logger.info(f'Token for {device_type}: {token}')
    return token


def get_movies(device_type):
    header = HEADER_TOKEN.copy()
    header['X-TOKEN'] = get_token(device_type)
    logger.info(f'Headers: {header}')
    request = requests.get(url=API_MOVIES_URL, headers=header)
    movies = request.json()
    logger.info(f'Movies list for {device_type}: {movies}')
    return movies
