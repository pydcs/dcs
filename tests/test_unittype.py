import textwrap
from pathlib import Path

import pytest

import dcs.countries
from dcs.liveries.livery import Livery
from dcs.liveries.liverycache import LiveryCache
from dcs.liveries.liveryscanner import LiveryScanner
from dcs.payloads import PayloadDirectories
from dcs.planes import F_16C_50
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


def test_load_payloads_skips_globbed_but_uncached_file(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """A payload .lua that scan_payload_dir globs but does not cache must be
    skipped, not raise.

    scan_payload_dir only records a payload file in _payload_cache when its
    content matches the `["unitType"] = "..."` regex, but load_payloads globs
    every *.lua and read the cache with a bare subscript. A globbed-but-uncached
    file (e.g. the shipping F-100D module, whose payload syntax the regex does
    not match) therefore raised KeyError and aborted the entire mission load.
    """
    payload_dir = tmp_path / "UnitPayloads"
    payload_dir.mkdir(parents=True)

    # A payload file the regex cannot cache: it has no `["unitType"] = "..."`
    # line, so scan_payload_dir globs it but stores no cache entry for it.
    (payload_dir / "Uncacheable.lua").write_text(
        textwrap.dedent(
            """\
            local unitPayloads = {
                name = "F-100D",
                payloads = {},
            }
            return unitPayloads
            """
        )
    )

    # A normal, cacheable payload file for the unit under test, so we also
    # confirm the valid file is still loaded while the uncacheable one is
    # simply skipped.
    (payload_dir / "Viper.lua").write_text(
        textwrap.dedent(
            f"""\
            local unitPayloads = {{
                ["unitType"] = "{F_16C_50.id}",
                ["payloads"] = {{
                    [1] = {{
                        ["name"] = "Test Loadout",
                        ["pylons"] = {{}},
                    }},
                }},
            }}
            return unitPayloads
            """
        )
    )

    # Point the scanner only at our temp dir (no real DCS install paths), and
    # reset the process-global caches so the scan re-runs against it.
    monkeypatch.setattr(PayloadDirectories, "preferred", payload_dir)
    monkeypatch.setattr(PayloadDirectories, "_dcs", [])
    monkeypatch.setattr(PayloadDirectories, "_mod", [])
    monkeypatch.setattr(PayloadDirectories, "_user", tmp_path / "does-not-exist")
    monkeypatch.setattr(PayloadDirectories, "fallback", None)
    monkeypatch.setattr(FlyingType, "_payload_cache", None)
    monkeypatch.setattr(F_16C_50, "payloads", None)

    # Must not raise KeyError on the globbed-but-uncached file.
    payloads = F_16C_50.load_payloads()

    # The cacheable file still loads; the uncacheable one was skipped.
    assert "Test Loadout" in payloads
