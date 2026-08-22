import pytest

from risk import calculate_risk


def test_critical_risk():
    score, level = calculate_risk(5, 5)

    assert score == 25
    assert level == "Critical"


def test_high_risk():
    score, level = calculate_risk(4, 3)

    assert score == 12
    assert level == "High"


def test_medium_risk():
    score, level = calculate_risk(3, 2)

    assert score == 6
    assert level == "Medium"


def test_low_risk():
    score, level = calculate_risk(1, 2)

    assert score == 2
    assert level == "Low"


def test_invalid_likelihood():
    with pytest.raises(ValueError):
        calculate_risk(6, 5)


def test_invalid_impact():
    with pytest.raises(ValueError):
        calculate_risk(5, 0)


def test_invalid_data_type():
    with pytest.raises(ValueError):
        calculate_risk("high", 5)