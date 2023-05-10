from pathlib import Path
from typing import Iterator
from unittest.mock import Mock, call, patch
from zipfile import ZipFile

import pytest

from dcs.liveries_scanner import Liveries, Livery, LiverySet


@pytest.fixture(autouse=True)
def clear_liveries_fixture() -> None:
    Liveries.map.clear()


@pytest.fixture(name="scan_lua_code_mock")
def scan_lua_code_mock_fixture() -> Iterator[Mock]:
    with patch("dcs.liveries_scanner.Liveries.scan_lua_code") as mock:
        yield mock


@pytest.fixture(name="scan_liveries_mock")
def scan_liveries_mock_fixture() -> Iterator[Mock]:
    with patch("dcs.liveries_scanner.Liveries.scan_liveries") as mock:
        yield mock


def test_find_unzipped_livery(tmp_path: Path, scan_lua_code_mock: Mock) -> None:
    description = tmp_path / "A-10CII/foobar/description.lua"
    description.parent.mkdir(parents=True)
    description.write_text("desc")
    Liveries.scan_liveries(str(tmp_path))
    scan_lua_code_mock.assert_called_once_with(
        "desc", str(description.parent), "A-10CII"
    )


def test_find_zipped_livery(tmp_path: Path, scan_lua_code_mock: Mock) -> None:
    zip_path = tmp_path / "A-10CII/foobar.zip"
    zip_path.parent.mkdir(parents=True)
    with ZipFile(zip_path, "w") as zip_file:
        zip_file.writestr("description.lua", "desc")
    Liveries.scan_liveries(str(tmp_path))
    scan_lua_code_mock.assert_called_once_with("desc", str(zip_path), "A-10CII")


def test_find_multiple_liveries(tmp_path: Path, scan_lua_code_mock: Mock) -> None:
    description0 = tmp_path / "A-10CII/foobar/description.lua"
    description0.parent.mkdir(parents=True)
    description0.write_text("desc")

    description1 = tmp_path / "A-10CII/baz/description.lua"
    description1.parent.mkdir(parents=True)
    description1.write_text("desc")

    Liveries.scan_liveries(str(tmp_path))
    scan_lua_code_mock.assert_has_calls(
        [
            call("desc", str(description0.parent), "A-10CII"),
            call("desc", str(description1.parent), "A-10CII"),
        ],
        any_order=True,
    )


def test_find_liveries_for_multiple_aircraft(
    tmp_path: Path, scan_lua_code_mock: Mock
) -> None:
    description0 = tmp_path / "A-10CII/foobar/description.lua"
    description0.parent.mkdir(parents=True)
    description0.write_text("desc")

    description1 = tmp_path / "A-10CIII/foobar/description.lua"
    description1.parent.mkdir(parents=True)
    description1.write_text("desc")

    Liveries.scan_liveries(str(tmp_path))
    scan_lua_code_mock.assert_has_calls(
        [
            call("desc", str(description0.parent), "A-10CII"),
            call("desc", str(description1.parent), "A-10CIII"),
        ],
        any_order=True,
    )


def test_find_no_liveries_for_aircraft(
    tmp_path: Path, scan_lua_code_mock: Mock
) -> None:
    (tmp_path / "A-10CII").mkdir(parents=True)
    Liveries.scan_liveries(str(tmp_path))
    scan_lua_code_mock.assert_not_called()


def test_find_no_aircraft_in_liveries_dir(
    tmp_path: Path, scan_lua_code_mock: Mock
) -> None:
    Liveries.scan_liveries(str(tmp_path))
    scan_lua_code_mock.assert_not_called()


def test_ignore_cockpit_liveries(tmp_path: Path) -> None:
    description = tmp_path / "A-10CII_COCKPIT/foobar/description.lua"
    description.parent.mkdir(parents=True)
    description.write_text("desc")

    with patch("dcs.liveries_scanner.LiverySet.add") as mock:
        Liveries.scan_liveries(str(tmp_path))
    mock.assert_not_called()


def test_case_insensitive_unit_id(tmp_path: Path, scan_lua_code_mock: Mock) -> None:
    description = tmp_path / "a-10Cii/foobar/description.lua"
    description.parent.mkdir(parents=True)
    description.write_text("desc")
    Liveries.scan_liveries(str(tmp_path))
    scan_lua_code_mock.assert_called_once_with(
        "desc", str(description.parent), "A-10CII"
    )


def test_campaign_alias_livery(tmp_path: Path, scan_lua_code_mock: Mock) -> None:
    description = tmp_path / "FW-190D-9/foobar/description.lua"
    description.parent.mkdir(parents=True)
    description.write_text("desc")
    Liveries.scan_liveries(str(tmp_path), campaign_path=True)
    scan_lua_code_mock.assert_called_once_with(
        "desc", str(description.parent), "FW-190D9"
    )


def test_campaign_alias_livery_only_for_campaign_paths(
    tmp_path: Path, scan_lua_code_mock: Mock
) -> None:
    description = tmp_path / "FW-190D-9/foobar/description.lua"
    description.parent.mkdir(parents=True)
    description.write_text("desc")
    Liveries.scan_liveries(str(tmp_path))
    scan_lua_code_mock.assert_called_once_with(
        "desc", str(description.parent), "FW-190D-9"
    )


def test_scan_mod_livery_directory(tmp_path: Path, scan_liveries_mock: Mock) -> None:
    paths = [
        tmp_path / "foo/Liveries",
        tmp_path / "bar",
        tmp_path / "baz/Liveries",
    ]
    for path in paths:
        path.mkdir(parents=True)

    Liveries.scan_mods_path(str(tmp_path))
    scan_liveries_mock.assert_has_calls(
        [
            call(str(paths[0])),
            call(str(paths[2])),
        ],
        any_order=True,
    )


def test_scan_empty_mod_livery_directory(
    tmp_path: Path, scan_liveries_mock: Mock
) -> None:
    Liveries.scan_mods_path(str(tmp_path / "nonexistent"))
    scan_liveries_mock.assert_not_called()


def test_scan_campaign_livery_directory(
    tmp_path: Path, scan_liveries_mock: Mock
) -> None:
    paths = [
        tmp_path / "foo/Liveries",
        tmp_path / "bar",
        tmp_path / "baz/Liveries",
    ]
    for path in paths:
        path.mkdir(parents=True)

    Liveries.scan_campaign_liveries(str(tmp_path))
    scan_liveries_mock.assert_has_calls(
        [
            call(str(paths[0]), campaign_path=True),
            call(str(paths[2]), campaign_path=True),
        ],
        any_order=True,
    )


def test_scan_empty_campaign_livery_directory(
    tmp_path: Path, scan_liveries_mock: Mock
) -> None:
    Liveries.scan_campaign_liveries(str(tmp_path / "nonexistent"))
    scan_liveries_mock.assert_not_called()


def test_scan_core_directories(tmp_path: Path, scan_liveries_mock) -> None:
    paths = [
        (tmp_path / "CoreMods/aircraft/mod1/Liveries", False),
        (tmp_path / "CoreMods/WWII Units/mod2/Liveries", False),
        (tmp_path / "Bazar/Liveries", False),
        (tmp_path / "Mods/campaigns/campaign/Liveries", True),
        (tmp_path / "CoreMods/tech/mod3/Liveries", False),
        (tmp_path / "Mods/tech/WWII Units/Liveries", False),
    ]

    calls = []
    for path, campaign in paths:
        path.mkdir(parents=True)
        if campaign:
            calls.append(call(str(path), campaign_path=True))
        else:
            calls.append(call(str(path)))

    Liveries.scan_dcs_installation(str(tmp_path))
    scan_liveries_mock.assert_has_calls(calls, any_order=True)


def test_scan_user_directories(tmp_path: Path, scan_liveries_mock) -> None:
    paths = [
        tmp_path / "Mods/aircraft/mod1/Liveries",
        tmp_path / "Liveries",
    ]

    calls = []
    for path in paths:
        path.mkdir(parents=True)
        calls.append(call(str(path)))

    Liveries.scan_custom_liveries(str(tmp_path))
    scan_liveries_mock.assert_has_calls(calls, any_order=True)


def test_scanning_livery_adds_one_livery() -> None:
    Liveries.map["unit"] = LiverySet()
    Liveries.scan_lua_code("", "foobar", "unit")

    assert len(Liveries.map.keys()) == 1
    assert len(Liveries.map["unit"]) == 1


def test_placeholder_livery() -> None:
    """Tests that liveries named "placeholder" are ignored."""
    Liveries.scan_lua_code("", "placeholder", "unit")
    Liveries.scan_lua_code("", "placeholder.zip", "unit")

    assert len(Liveries.map.keys()) == 0


def test_named_livery() -> None:
    """Tests description decoding when the livery lua sets the name."""
    Liveries.map["unit"] = LiverySet()
    Liveries.scan_lua_code('name = "Foobar"', "foobar", "unit")

    livery = Liveries.map["unit"].pop()
    assert livery.name == "Foobar"


def test_livery_defaults() -> None:
    """Tests description decoding when the livery is not explicitly named."""
    Liveries.map["unit"] = LiverySet()
    Liveries.scan_lua_code("", "foobar", "unit")

    livery: Livery = Liveries.map["unit"].pop()
    assert livery.name == "foobar"
    assert livery.countries is None
    assert livery.order == 0


def test_livery_id_from_directory() -> None:
    """Tests that the livery ID is set appropriately for a directory livery."""
    Liveries.map["unit"] = LiverySet()
    Liveries.scan_lua_code("", str(Path("foo/bar")), "unit")

    livery = Liveries.map["unit"].pop()
    assert livery.id == "bar"


def test_livery_id_from_zip() -> None:
    """Tests that the livery ID for a zipped livery does not include .zip."""
    Liveries.map["unit"] = LiverySet()
    Liveries.scan_lua_code("", str(Path("foo/bar.zip")), "unit")

    livery = Liveries.map["unit"].pop()
    assert livery.id == "bar"


def test_parse_single_country() -> None:
    Liveries.map["unit"] = LiverySet()
    Liveries.scan_lua_code('countries = {"USA"}', "foobar", "unit")

    livery = Liveries.map["unit"].pop()
    assert livery.countries == {"USA"}


def test_parse_multiple_countries() -> None:
    Liveries.map["unit"] = LiverySet()
    Liveries.scan_lua_code('countries = {"USA", "RUS"}', "foobar", "unit")

    livery = Liveries.map["unit"].pop()
    assert livery.countries == {"USA", "RUS"}


def test_sort_order() -> None:
    Liveries.map["unit"] = LiverySet()
    Liveries.scan_lua_code("order = 2", "foobar", "unit")

    livery = Liveries.map["unit"].pop()
    livery.order == 2


def test_ansi_encoded_description(tmp_path: Path, scan_lua_code_mock: Mock) -> None:
    (tmp_path / "description.lua").write_bytes("Š".encode("ansi"))
    Liveries.scan_lua_description(str(tmp_path), "foobar")
    scan_lua_code_mock.assert_called_once_with("Š", str(tmp_path), "foobar")


def test_livery_valid_for_country() -> None:
    assert Livery("", "", 0, None).valid_for_country("fadfasdf")
    assert Livery("", "", 0, {"USA"}).valid_for_country("USA")
    assert not Livery("", "", 0, {"USA"}).valid_for_country("RUS")
    assert Livery("", "", 0, {"USA", "RUS"}).valid_for_country("RUS")
