import pytest
from click.testing import CliRunner
from tokened import cli, __version__


@pytest.fixture
def runner():
    return CliRunner()


def test_cli(runner):
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert not result.exception
    assert result.output.strip() == 'Hello, world.'


def test_cli_with_option(runner):
    result = runner.invoke(cli.main, ['--as-cowboy'])
    assert not result.exception
    assert result.exit_code == 0
    assert result.output.strip() == 'Howdy, world.'


def test_cli_with_arg(runner):
    result = runner.invoke(cli.main, ['Matt'])
    assert result.exit_code == 0
    assert not result.exception
    assert result.output.strip() == 'Hello, Matt.'


def test_cli_version(runner):
    result = runner.invoke(cli.main, ['--version'])
    assert result.exit_code == 0
    assert not result.exception
    assert __version__ in result.output
