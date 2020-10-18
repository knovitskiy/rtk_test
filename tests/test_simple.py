from http_requests import get_movies
import pytest


pytestmark = pytest.mark.usefixtures("data_for_tests")


device_type = 'tv'


def test_simple_test():
    movies_list = get_movies(device_type)
    print(movies_list)
