from http_requests import get_movies


device_type = 'tv'


def test_simple_test():
    movies_list = get_movies(device_type)
    assert movies_list['items'] == []
