import dcs.countries


def test_countries_eq() -> None:
    assert dcs.countries.get_by_id(0) == dcs.countries.get_by_id(0)
    assert dcs.countries.get_by_id(0) != dcs.countries.get_by_id(1)
    assert dcs.countries.get_by_id(0) != "dynamic typing is stupid"


def test_country_by_name() -> None:
    dcs.countries.get_by_name("Russia") == dcs.countries.get_by_id(0)


def test_country_by_short_name() -> None:
    dcs.countries.get_by_short_name("RUS") == dcs.countries.get_by_id(0)
