from http_requests import get_movies
from data import Films
from constants import TV_DEVICE, MOBILE_DEVICE, STB_DEVICE
import pytest


pytestmark = pytest.mark.usefixtures("data_for_tests")


@pytest.mark.parametrize('device_type', [TV_DEVICE, MOBILE_DEVICE, STB_DEVICE])
def test_film_in_list(device_type):
    movies_list = get_movies(device_type)
    assert Films.RELEASED['name'] in movies_list


@pytest.mark.parametrize('device_type', [TV_DEVICE, MOBILE_DEVICE, STB_DEVICE])
def test_film_not_released(device_type):
    movies_list = get_movies(device_type)
    assert Films.NOT_RELEASED['name'] not in movies_list


@pytest.mark.parametrize('device_type', [TV_DEVICE, MOBILE_DEVICE, STB_DEVICE])
def test_film_ended(device_type):
    movies_list = get_movies(device_type)
    assert Films.ENDED['name'] not in movies_list


@pytest.mark.parametrize('token', ['123', ''])
def test_invalid_token_value(token):
    response = get_movies(TV_DEVICE, token_value=token)
    assert 'Токен не найден' in response['message']


def test_invalid_token_key():
    response = get_movies(TV_DEVICE, token_value='123')
    assert 'Токен не найден' in response['message']