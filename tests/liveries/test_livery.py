from pathlib import Path
from zipfile import ZipFile

from dcs.liveries.livery import Livery
from dcs.liveries.liveryset import LiverySet


def test_placeholder_livery() -> None:
    """Tests that liveries named "placeholder" are ignored."""
    assert Livery.from_lua("", "placeholder") is None
    assert Livery.from_lua("", "placeholder.zip") is None


def test_named_livery() -> None:
    """Tests description decoding when the livery lua sets the name."""
    livery = Livery.from_lua('name = "Foobar"', "foobar")
    assert livery is not None
    assert livery.name == "Foobar"


def test_livery_defaults() -> None:
    """Tests description decoding when the livery is not explicitly named."""
    livery = Livery.from_lua("", "foobar")
    assert livery is not None
    assert livery.name == "foobar"
    assert livery.countries is None
    assert livery.order == 0


def test_livery_id_from_directory() -> None:
    """Tests that the livery ID is set appropriately for a directory livery."""
    livery = Livery.from_lua("", str(Path("foo/bar")))
    assert livery is not None
    assert livery.id == "bar"


def test_livery_id_from_zip() -> None:
    """Tests that the livery ID for a zipped livery does not include .zip."""
    livery = Livery.from_lua("", str(Path("foo/bar.zip")))
    assert livery is not None
    assert livery.id == "bar"


def test_parse_single_country() -> None:
    livery = Livery.from_lua('countries = {"USA"}', "foobar")
    assert livery is not None
    assert livery.countries == {"USA"}


def test_parse_multiple_countries() -> None:
    livery = Livery.from_lua('countries = {"USA", "RUS"}', "foobar")
    assert livery is not None
    assert livery.countries == {"USA", "RUS"}


def test_sort_order() -> None:
    livery = Livery.from_lua("order = 2", "foobar")
    assert livery is not None
    livery.order == 2


def test_livery_valid_for_country() -> None:
    assert Livery("", "", 0, None).valid_for_country("fadfasdf")
    assert Livery("", "", 0, {"USA"}).valid_for_country("USA")
    assert not Livery("", "", 0, {"USA"}).valid_for_country("RUS")
    assert Livery("", "", 0, {"USA", "RUS"}).valid_for_country("RUS")


def test_ansi_encoded_description(tmp_path: Path) -> None:
    (tmp_path / "description.lua").write_bytes("name = 'Š'".encode("ansi"))
    livery = Livery.from_path(str(tmp_path))
    assert livery is not None
    assert livery.name == "Š"


def test_find_unzipped_livery(tmp_path: Path) -> None:
    description = tmp_path / "description.lua"
    description.touch()
    assert Livery.from_path(str(tmp_path)) is not None


def test_find_zipped_livery(tmp_path: Path) -> None:
    zip_path = tmp_path / "foo.zip"
    with ZipFile(zip_path, "w") as zip_file:
        with zip_file.open("description.lua", "w") as description:
            pass
    assert Livery.from_path(str(zip_path)) is not None


def test_livery_id_forced_lower_case(tmp_path: Path) -> None:
    path = tmp_path / "FOO"
    path.mkdir()
    description = path / "description.lua"
    description.touch()
    livery = Livery.from_path(str(path))
    assert livery is not None
    assert livery.id.islower()
