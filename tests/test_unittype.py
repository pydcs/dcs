import textwrap
from pathlib import Path

import dcs.countries
from dcs.liveries.livery import Livery
from dcs.liveries.liverycache import LiveryCache
from dcs.liveries.liveryscanner import LiveryScanner
from dcs.payloads import PayloadDirectories
from dcs.planes import F_16C_50
from dcs.task import CAP
from dcs.unittype import FlyingType


def test_plane_liveries(tmp_path: Path) -> None:
    dcs_install = tmp_path / "install"
    saved_games = tmp_path / "savedgames"

    viper_liveries = (
        dcs_install
        / "CoreMods/aircraft"
        / F_16C_50.id
        / "Liveries"
        / F_16C_50.livery_name
    )

    foo_livery = viper_liveries / "foo"
    foo_livery.mkdir(parents=True)
    (foo_livery / "description.lua").touch()

    bar_livery = viper_liveries / "bar"
    bar_livery.mkdir(parents=True)
    (bar_livery / "description.lua").touch()

    LiveryCache._cache = LiveryScanner().load_from(str(dcs_install), str(saved_games))

    expected = {
        Livery("foo", "foo", 0, None),
        Livery("bar", "bar", 0, None),
    }
    assert set(F_16C_50.iter_liveries()) == expected


def test_plane_liveries_for_country(tmp_path: Path) -> None:
    dcs_install = tmp_path / "install"
    saved_games = tmp_path / "savedgames"

    viper_liveries = (
        dcs_install
        / "CoreMods/aircraft"
        / F_16C_50.id
        / "Liveries"
        / F_16C_50.livery_name
    )

    foo_livery = viper_liveries / "foo"
    foo_livery.mkdir(parents=True)
    (foo_livery / "description.lua").write_text(
        textwrap.dedent(
            """\
            countries = {"USA", "FRA"}
            """
        )
    )

    bar_livery = viper_liveries / "bar"
    bar_livery.mkdir(parents=True)
    (bar_livery / "description.lua").write_text(
        textwrap.dedent(
            """\
            countries = {"RUS"}
            """
        )
    )

    baz_livery = viper_liveries / "baz"
    baz_livery.mkdir(parents=True)
    (baz_livery / "description.lua").touch()

    LiveryCache._cache = LiveryScanner().load_from(str(dcs_install), str(saved_games))

    expected = {
        Livery("foo", "foo", 0, None),
        Livery("baz", "baz", 0, None),
    }
    assert (
        set(F_16C_50.iter_liveries_for_country(dcs.countries.get_by_short_name("USA")))
        == expected
    )


def test_non_standard_payload_definition(tmp_path: Path) -> None:
    PayloadDirectories.set_preferred(tmp_path)

    (tmp_path / "test.lua").write_text(textwrap.dedent("""\
            unitPayloads = abc
            """))
    # Clears cached payloads to force re-load
    FlyingType._payload_cache = None
    F_16C_50.payloads = None
    F_16C_50._payload_cache = {}
    F_16C_50.load_payloads()  # test is that load_payloads() runs without failing


def test_standard_payload_definition(tmp_path: Path) -> None:
    PayloadDirectories.set_preferred(tmp_path)

    (tmp_path / "test.lua").write_text(textwrap.dedent("""\
            local unitPayloads = {
                ["name"] = "F-16C_50",
                ["payloads"] = {
                    [1] = {
                        ["displayName"] = "test_payload",
                        ["name"] = "test_payload",
                        ["pylons"] = {
                            [1] = {
                                ["CLSID"] = "{C8E06185-7CD6-4C90-959F-044679E90751}",
                                ["num"] = 1,
                            },
                        },
                        ["tasks"] = {
                            [1] = 11,
                        },
                    },
                },    
            	["unitType"] = "F-16C_50",
            }
            return unitPayloads
            """))
    # Clears cached payloads to force re-load
    FlyingType._payload_cache = None
    F_16C_50.payloads = None
    payloads = F_16C_50.load_payloads()
    assert "test_payload" in payloads
    assert payloads["test_payload"] == {'displayName': 'test_payload', 'name': 'test_payload', 'pylons': {1: {'CLSID': '{C8E06185-7CD6-4C90-959F-044679E90751}', 'num': 1}}, 'tasks': {1: 11}}
    assert F_16C_50.loadout_by_name("test_payload") == [(1, {'clsid': '{C8E06185-7CD6-4C90-959F-044679E90751}'})]
    assert F_16C_50.loadout(CAP) == [(1, {'clsid': '{C8E06185-7CD6-4C90-959F-044679E90751}'})]
    

def test_payload_definition_with_fuze_settings(tmp_path: Path) -> None:
    PayloadDirectories.set_preferred(tmp_path)

    (tmp_path / "test.lua").write_text(textwrap.dedent("""\
            local unitPayloads = {
                ["name"] = "F-16C_50",
                ["payloads"] = {
                    [1] = {
                        ["displayName"] = "test_payload",
                        ["name"] = "test_payload",
                        ["pylons"] = {
                            [1] = {
                                ["CLSID"] = "{C8E06185-7CD6-4C90-959F-044679E90751}",
                                ["num"] = 1,
                                ["settings"] = {
                                    ["first"] = 1,
                                    ["second"] = "A",
                                },
                            },
                        },
                        ["tasks"] = {
                            [1] = 11,
                        },
                    },
                },    
            	["unitType"] = "F-16C_50",
            }
            return unitPayloads
            """))
    # Clears cached payloads to force re-load
    FlyingType._payload_cache = None
    F_16C_50.payloads = None
    payloads = F_16C_50.load_payloads()
    assert "test_payload" in payloads
    assert payloads["test_payload"] == {'displayName': 'test_payload', 'name': 'test_payload', 'pylons': {1: {'CLSID': '{C8E06185-7CD6-4C90-959F-044679E90751}', 'num': 1, 'settings': {'first': 1, 'second': 'A'}}}, 'tasks': {1: 11}}
    assert F_16C_50.loadout_by_name("test_payload") == [(1, {'clsid': '{C8E06185-7CD6-4C90-959F-044679E90751}', 'settings': {'first': 1, 'second': 'A'}})]
    assert F_16C_50.loadout(CAP) == [(1, {'clsid': '{C8E06185-7CD6-4C90-959F-044679E90751}', 'settings': {'first': 1, 'second': 'A'}})]
