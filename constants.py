from urllib.parse import urljoin


BASE_URL = 'http://tools.restream.ru:4001'
API = 'api'
QA = 'qa'
MOVIES = 'movies'
SERVICES = 'services'
TOKEN = 'token'

API_MOVIES_URL = f'{BASE_URL}/{API}/{MOVIES}'
API_TOKEN_URL = f'{BASE_URL}/{API}/{TOKEN}'

QA_MOVIES_URL = f'{BASE_URL}/{QA}/{MOVIES}'
QA_SERVICES_URL = f'{BASE_URL}/{QA}/{SERVICES}'

BODY_TOKEN = {"device_type": "device_type"}

HEADER_TOKEN = {"X-TOKEN": "token"}
