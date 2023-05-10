import re

import pytest
from click.testing import CliRunner
from ccfcoef.cli import cli


@pytest.fixture(scope='module')
def runner():
    return CliRunner()


def test_cpu_averages(runner):
    result = runner.invoke(cli, ['cpu-averages', '--family', 'amd-epyc-gen1'])
    assert result.exit_code == 0
    # Specific values are asserted in test_power_averages.py
    assert 'Averages for: EPYC 1st Gen' in result.output
    assert 'Average: Min Watts =' in result.output
    assert 'Average: Max Watts =' in result.output
    assert 'Average: Max Watts (GCP) =' in result.output
    assert 'Average: GB/chip =' in result.output


def test_list_specs(runner):
    result = runner.invoke(cli, ['list-specs'])
    # verbose output
    assert result.exit_code == 0
    assert re.search(r"SPECpower-(\d{4}-\d{2}-\d{2}).csv version:(\d{4}-\d{2}-\d{2})", result.output)

    # just the versions
    result = runner.invoke(cli, ['list-specs', '--raw'])
    assert re.search(r"\d{4}-\d{2}-\d{2}", result.output)
