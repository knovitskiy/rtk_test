import pytest
from data import Films, Services
from http_requests import create_movie, create_service, delete_all_movies, delete_all_services
import time
from constants import WAITING_DATA_CREATED


@pytest.fixture()
def data_for_tests():

    # creating services
    services = [Services.TV, Services.MOBILE, Services.STB]
    services_ids = []
    for service in services:
        services_ids.append(create_service(service))
    films = [Films.RELEASED, Films.NOT_RELEASED, Films.ENDED]

    # creating movies for tv
    for film in films:
        new_film = film.copy()
        new_film['services'][0] = services_ids[0]
        create_movie(new_film)

    # creating movies for mobile
    for film in films:
        new_film = film.copy()
        new_film['services'][0] = services_ids[1]
        create_movie(new_film)

    # creating movies for stb
    for film in films:
        new_film = film.copy()
        new_film['services'][0] = services_ids[2]
        create_movie(new_film)

    time.sleep(WAITING_DATA_CREATED)

    yield

    delete_all_movies()
    delete_all_services()