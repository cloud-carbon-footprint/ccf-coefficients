import math

import pytest

from ccfcoef.cli import CPU_FAMILIES, calculate_cpus_families_power

# Expected values for each family in the order of CPU_FAMILIES
# family, min_watts, max_watts, max_watts_gcp_adjusted, gb_chip
EXPECTED_AVERAGE_POWER = [
    (CPU_FAMILIES[0].name, 0.85, 2.6, 2.54, 92.44),
    (CPU_FAMILIES[1].name, 0.47, 1.69, 1.58, 129.78),
    (CPU_FAMILIES[2].name, 0.46, 1.96, 1.83, 137.14),
    (CPU_FAMILIES[3].name, 0.74, 2.28, 2.2, 152.2),
    (CPU_FAMILIES[4].name, 3.68, 8.96, 8.86, 74.62),
    (CPU_FAMILIES[5].name, 0.74, 1.71, 1.65, 91.43),
    (CPU_FAMILIES[6].name, 2.21, 8.63, 8.6, 17.07),
    (CPU_FAMILIES[7].name, 1.71, 5.56, 5.51, 13.33),
    (CPU_FAMILIES[8].name, 1.86, 5.6, 5.56, 31.06),
    (CPU_FAMILIES[9].name, 0.71, 3.69, 3.39, 69.65),
    (CPU_FAMILIES[10].name, 0.55, 4.01, 3.76, 78.67),
    (CPU_FAMILIES[11].name, 1.82, 5.86, 5.85, 16.0),
    (CPU_FAMILIES[12].name, 0.69, 4.06, 3.75, 105.97),
    (CPU_FAMILIES[13].name, 1.14, 5.42, 5.41, 19.56),
    (CPU_FAMILIES[14].name, 0.77, 3.76, 3.65, 136.0),
    (CPU_FAMILIES[15].name, 1.04, 4.16, 4.06, 130.8),
    (CPU_FAMILIES[16].name, 0.58, 2.53, 2.37, 221.14),
    (CPU_FAMILIES[17].name, 0.81, 4.48, 4.38, 160.0),
]


@pytest.fixture(scope='module')
def average_power():
    return calculate_cpus_families_power(CPU_FAMILIES)


@pytest.mark.parametrize('family, min_watts, max_watts, max_watts_gcp_adjusted, gb_chip', EXPECTED_AVERAGE_POWER)
def test_cpu_average(family, min_watts, max_watts, max_watts_gcp_adjusted, gb_chip, average_power):
    assert float('{:,.2f}'.format(average_power[family].min_watts)) == min_watts
    assert float('{:,.2f}'.format(average_power[family].max_watts)) == max_watts
    assert float('{:,.2f}'.format(average_power[family].max_watts_gcp_adjusted)) == max_watts_gcp_adjusted
    assert float('{:,.2f}'.format(average_power[family].gb_chip)) == gb_chip
