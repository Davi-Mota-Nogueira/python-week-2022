from typer.testing import CliRunner

from beerlog.cli import main

runner = CliRunner()


def test_add_beer():
    result = runner.invoke(
        main, ["add", "Skol", "KornIPA", "--flavor=4", "--image=5", "--cost=6"]
    )
    assert result.exit_code == 0
    assert "Beer added" in result.stdout
