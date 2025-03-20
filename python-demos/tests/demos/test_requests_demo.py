from unittest.mock import patch

import requests
import responses

from demos.requests_demo import check_api_health

# def test_check_api_health():
#     assert check_api_health("https://www.baidu.com") == True
#     assert check_api_health("https://www.google.com") == True
#     assert check_api_health("https://www.bing.com") == True
#     assert check_api_health("https://www.google.com/wrongapi") == False
#     assert check_api_health("https://www.not.exist/api") == False


@responses.activate
def test_check_api_health_with_responses():
    responses.add(responses.GET, "https://www.google.com", status=200)
    assert check_api_health("https://www.google.com") is True
    responses.add(responses.GET, "https://www.google.com/wrongapi", status=404)
    assert check_api_health("https://www.google.com/wrongapi") is False
    # responses.add(responses.GET, 'https://www.not.exist/api', status=500)
    assert check_api_health("https://www.not.exist/api") is False


def test_check_api_health_with_pytest_mock(mocker):
    mock_get = mocker.patch("requests.get")
    mock_get.return_value.status_code = 200
    assert check_api_health("https://www.google.com") is True

    mock_get.return_value.status_code = 404
    assert check_api_health("https://www.google.com/wrongapi") is False

    mock_get.side_effect = requests.RequestException
    assert check_api_health("https://www.not.exist/api") is False


def test_check_api_health_with_unitest_mock():
    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        assert check_api_health("https://www.google.com") is True

        mock_get.return_value.status_code = 404
        assert check_api_health("https://www.google.com/wrongapi") is False

        mock_get.side_effect = requests.RequestException
        assert check_api_health("https://www.not.exist/api") is False
