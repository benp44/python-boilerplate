import click.testing
import pytest

from example_cli import console


@pytest.fixture
def mock_cat_fact_model(mocker):
    mock = mocker.patch("example_cli.cat_fact_model.get_fact")
    mock.return_value = "some test fact"
    return mock


@pytest.fixture
def runner():
    return click.testing.CliRunner()


def test_main_succeeds(mock_cat_fact_model):
    runner = click.testing.CliRunner()
    result = runner.invoke(console.main)
    assert result.exit_code == 0


def test_main_prints_fact(runner, mock_cat_fact_model):
    result = runner.invoke(console.main)
    assert "some test fact" in result.output
