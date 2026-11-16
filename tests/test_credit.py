import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from credit import calculate_risk  # noqa: E402


# ---------- Partie A : cas normaux ----------

def test_high_risk():
    result = calculate_risk(1000, 700, 30)
    assert result == "HIGH"


def test_medium_risk():
    result = calculate_risk(1000, 400, 30)
    assert result == "MEDIUM"


def test_low_risk():
    result = calculate_risk(1000, 100, 30)
    assert result == "LOW"


# ---------- Partie B : cas limites ----------

def test_zero_income():
    assert calculate_risk(0, 500, 30) == -1


def test_negative_income():
    assert calculate_risk(-1000, 500, 30) == -1


def test_zero_debt():
    assert calculate_risk(1000, 0, 30) == "LOW"


def test_ratio_exactly_0_3():
    # 0.3 n'est pas > 0.3 -> LOW
    assert calculate_risk(1000, 300, 30) == "LOW"


def test_ratio_exactly_0_6():
    # 0.6 n'est pas > 0.6 -> MEDIUM
    assert calculate_risk(1000, 600, 30) == "MEDIUM"


@pytest.mark.parametrize(
    "income, debt, expected",
    [
        (1000, 301, "MEDIUM"),  # juste au-dessus de 0.3
        (1000, 601, "HIGH"),    # juste au-dessus de 0.6
        (1000, 1500, "HIGH"),   # dette > revenu
    ],
)
def test_just_above_thresholds(income, debt, expected):
    assert calculate_risk(income, debt, 30) == expected
