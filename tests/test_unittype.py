from pathlib import Path

from dcs.liveries.livery import Livery
from dcs.liveries.liverycache import LiveryCache
from dcs.liveries.liveryscanner import LiveryScanner
from dcs.planes import F_16C_50


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
