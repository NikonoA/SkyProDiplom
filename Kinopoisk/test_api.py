import requests

headers = {
    'X-API-KEY': "FJY7AJT-RRFM9KD-GET030W-MHTGQ4N"
    }
base_url = "https://api.kinopoisk.dev/v1.4/movie"
base_url1 = "https://api.kinopoisk.dev/v1.4/movie/search?page=1&limit=10"
for_movie = "selectFields=movies"
title = "nomination.award.title"
aw_year = "nomination.award.year"


def test_api_search_by_id():
    response = requests.get(f"{base_url}/6224943", headers=headers)
    assert response.status_code == 200


def test_api_search_by_title():
    movie = "Now You See Me"
    response = requests.get(f"{base_url1}&query={movie}", headers=headers)
    assert response.status_code == 200


def test_api_by_awards():
    award = "Лучший фильм"
    year = 2024
    response = requests.get(
        f"{base_url1}&{for_movie}&{title}={award}&{aw_year}={year}",
        headers=headers,
    )
    assert response.status_code == 200


def test_api_search_with_filters():
    type = "anime"
    status = "completed"
    genres = "комедия"
    response = requests.get(
        f"{base_url1}&type={type}&status={status}&genres.name={genres}",
        headers=headers,
    )
    assert response.status_code == 200


def test_api_search_collection():
    category = "Сериалы"
    response = requests.get(f"{base_url1}&category={category}",
                            headers=headers)
    assert response.status_code == 200
