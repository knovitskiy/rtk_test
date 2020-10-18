import requests
import logging
from constants import BODY_TOKEN, API_TOKEN_URL, API_MOVIES_URL, QA_SERVICES_URL, QA_MOVIES_URL, HEADER_TOKEN


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


def get_movies(device_type: str):
    header = HEADER_TOKEN.copy()
    header['X-TOKEN'] = get_token(device_type)
    logger.info(f'Headers: {header}')
    request = requests.get(url=API_MOVIES_URL, headers=header)
    movies_json = request.json()['items']
    movies_list = []
    for movie_item in movies_json:
        movies_list.append(movie_item['name'])
    logger.info(f'Movies list for {device_type}: {movies_list}')
    return movies_list


def create_service(service: dict):
    request = requests.post(url=QA_SERVICES_URL, json=service)
    logger.info(f'Creating a service...\n{request.text}')
    return request.json()['id']


def create_movie(movie: dict):
    request = requests.post(url=QA_MOVIES_URL, json=movie)
    logger.info(f'Creating a movie...\n{request.text}')


def delete_all_services():
    request = requests.delete(url=QA_SERVICES_URL)
    logger.info(f'Deleting all services...\n{request.text}')


def delete_all_movies():
    request = requests.delete(url=QA_MOVIES_URL)
    logger.info(f'Deleting all movies...\n{request.text}')
