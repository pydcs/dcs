import dcs.countries


def test_countries_eq() -> None:
    assert dcs.countries.get_by_id(0) == dcs.countries.get_by_id(0)
    assert dcs.countries.get_by_id(0) != dcs.countries.get_by_id(1)
    assert dcs.countries.get_by_id(0) != "dynamic typing is stupid"
