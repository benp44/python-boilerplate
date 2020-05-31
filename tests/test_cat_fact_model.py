import pytest

from example_cli import cat_fact_model


@pytest.fixture
def mock_requests_get(mocker):
    mock = mocker.patch("requests.get")
    mock.return_value.__enter__.return_value.json.return_value = {"text": "some test fact"}
    return mock


def test_get_fact_gets_fact_from_cat_fact_api(mock_requests_get):
    cat_fact_model.get_fact()
    assert mock_requests_get.called_once
    args, _ = mock_requests_get.call_args
    assert "https://cat-fact.herokuapp.com/facts/random" == args[0]


def test_get_fact_returns_nothing_on_request_error(mock_requests_get):
    mock_requests_get.side_effect = Exception("Boom")
    fact = cat_fact_model.get_fact()
    assert fact == ""
