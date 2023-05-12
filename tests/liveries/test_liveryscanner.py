from pathlib import Path
from typing import Iterator
from unittest.mock import ANY, Mock, call, patch

import pytest

from dcs.liveries.livery import Livery
from dcs.liveries.liveryscanner import LiveryScanner


@pytest.fixture(name="livery_from_path_mock")
def livery_from_path_mock_fixture() -> Iterator[Mock]:
    with patch("dcs.liveries.livery.Livery.from_path") as mock:
        mock.return_value = Livery("", "", 0, None)
        yield mock


@pytest.fixture(name="scan_liveries_mock")
def scan_liveries_mock_fixture() -> Iterator[Mock]:
    with patch("dcs.liveries.liveryscanner.LiveryScanner.scan_liveries") as mock:
        yield mock


@pytest.fixture(name="register_livery_mock")
def register_livery_mock_fixture() -> Iterator[Mock]:
    with patch("dcs.liveries.liveryscanner.LiveryScanner.register_livery") as mock:
        yield mock


def test_find_multiple_liveries(tmp_path: Path, livery_from_path_mock: Mock) -> None:
    description0 = tmp_path / "A-10CII/foobar/description.lua"
    description0.parent.mkdir(parents=True)
    description0.write_text("desc")

    description1 = tmp_path / "A-10CII/baz/description.lua"
    description1.parent.mkdir(parents=True)
    description1.write_text("desc")

    LiveryScanner().scan_liveries(str(tmp_path))
    livery_from_path_mock.assert_has_calls(
        [
            call(str(description0.parent)),
            call(str(description1.parent)),
        ],
        any_order=True,
    )


def test_find_liveries_for_multiple_aircraft(
    tmp_path: Path, livery_from_path_mock: Mock
) -> None:
    description0 = tmp_path / "A-10CII/foobar/description.lua"
    description0.parent.mkdir(parents=True)
    description0.write_text("desc")

    description1 = tmp_path / "A-10CIII/foobar/description.lua"
    description1.parent.mkdir(parents=True)
    description1.write_text("desc")

    LiveryScanner().scan_liveries(str(tmp_path))
    livery_from_path_mock.assert_has_calls(
        [
            call(str(description0.parent)),
            call(str(description1.parent)),
        ],
        any_order=True,
    )


def test_find_no_liveries_for_aircraft(
    tmp_path: Path, livery_from_path_mock: Mock
) -> None:
    (tmp_path / "A-10CII").mkdir(parents=True)
    LiveryScanner().scan_liveries(str(tmp_path))
    livery_from_path_mock.assert_not_called()


def test_find_no_aircraft_in_liveries_dir(
    tmp_path: Path, livery_from_path_mock: Mock
) -> None:
    LiveryScanner().scan_liveries(str(tmp_path))
    livery_from_path_mock.assert_not_called()


def test_ignore_cockpit_liveries(tmp_path: Path) -> None:
    description = tmp_path / "A-10CII_COCKPIT/foobar/description.lua"
    description.parent.mkdir(parents=True)
    description.write_text("desc")

    with patch("dcs.liveries.liveryset.LiverySet.add") as mock:
        LiveryScanner().scan_liveries(str(tmp_path))
    mock.assert_not_called()


def test_case_insensitive_unit_id(tmp_path: Path, register_livery_mock: Mock) -> None:
    description = tmp_path / "a-10Cii/foobar/description.lua"
    description.parent.mkdir(parents=True)
    description.touch()
    LiveryScanner().scan_liveries(str(tmp_path))
    register_livery_mock.assert_called_once_with("A-10CII", ANY)


def test_campaign_alias_livery(tmp_path: Path, register_livery_mock: Mock) -> None:
    description = tmp_path / "FW-190D-9/foobar/description.lua"
    description.parent.mkdir(parents=True)
    description.touch()
    LiveryScanner().scan_liveries(str(tmp_path), campaign_path=True)
    register_livery_mock.assert_called_once_with("FW-190D9", ANY)


def test_campaign_alias_livery_only_for_campaign_paths(
    tmp_path: Path, register_livery_mock: Mock
) -> None:
    description = tmp_path / "FW-190D-9/foobar/description.lua"
    description.parent.mkdir(parents=True)
    description.touch()
    LiveryScanner().scan_liveries(str(tmp_path))
    register_livery_mock.assert_called_once_with("FW-190D-9", ANY)


def test_scan_mod_livery_directory(tmp_path: Path, scan_liveries_mock: Mock) -> None:
    paths = [
        tmp_path / "foo/Liveries",
        tmp_path / "bar",
        tmp_path / "baz/Liveries",
    ]
    for path in paths:
        path.mkdir(parents=True)

    LiveryScanner().scan_mods_path(str(tmp_path))
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
    LiveryScanner().scan_mods_path(str(tmp_path / "nonexistent"))
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

    LiveryScanner().scan_campaign_liveries(str(tmp_path))
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
    LiveryScanner().scan_campaign_liveries(str(tmp_path / "nonexistent"))
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

    LiveryScanner().scan_dcs_installation(str(tmp_path))
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

    LiveryScanner().scan_custom_liveries(str(tmp_path))
    scan_liveries_mock.assert_has_calls(calls, any_order=True)
