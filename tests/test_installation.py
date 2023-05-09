import textwrap
from pathlib import Path
from typing import Any, Callable, Iterator, Optional, TypeVar
from unittest.mock import Mock, patch

import pytest

from dcs.installation import (
    DCS_BETA_REGISTRY_KEY_NAME,
    DCS_STABLE_REGISTRY_KEY_NAME,
    STEAM_REGISTRY_KEY_NAME,
    get_dcs_install_directory,
    get_dcs_saved_games_directory,
)

T = TypeVar("T")


def configure_registry_mock(
    mock: Mock,
    steam: Optional[Path] = None,
    standalone_stable: Optional[Path] = None,
    standalone_beta: Optional[Path] = None,
) -> None:
    def registry_mock(
        key: str, value: str, ctor: Callable[[Any], T] = lambda x: x
    ) -> Optional[T]:
        if (
            key == STEAM_REGISTRY_KEY_NAME
            and value == "SteamPath"
            and steam is not None
        ):
            return ctor(steam)
        if (
            key == DCS_STABLE_REGISTRY_KEY_NAME
            and value == "Path"
            and standalone_stable is not None
        ):
            return ctor(standalone_stable)
        if (
            key == DCS_BETA_REGISTRY_KEY_NAME
            and value == "Path"
            and standalone_beta is not None
        ):
            return ctor(standalone_beta)
        return None

    mock.side_effect = registry_mock


@pytest.fixture(name="steam_dcs_install")
def steam_dcs_install_fixture(tmp_path: Path) -> Iterator[Path]:
    escaped_path = str(tmp_path).replace("\\", "\\\\")
    vdf_path = tmp_path / "steamapps/libraryfolders.vdf"
    vdf_path.parent.mkdir(parents=True)
    vdf_path.write_text(
        textwrap.dedent(
            f"""\
            "LibraryFolders"
            {{
                "TimeNextStatsReport"        "1561832478"
                "ContentStatsID"        "-158337411110787451"
                "1"        "D:\\\\Games\\\\Steam"
                "2"        "{escaped_path}"
            }}
            """
        )
    )

    dcs_install_path = tmp_path / "steamapps/common/DCSWorld"
    dcs_install_path.mkdir(parents=True)

    with patch("dcs.installation.read_current_user_value") as mock:
        configure_registry_mock(mock, steam=tmp_path)
        yield dcs_install_path


@pytest.fixture(name="stable_dcs_install")
def stable_dcs_install_fixture(tmp_path: Path) -> Iterator[Path]:
    with patch("dcs.installation.read_current_user_value") as mock:
        configure_registry_mock(mock, standalone_stable=tmp_path)
        yield tmp_path


@pytest.fixture(name="beta_dcs_install")
def beta_dcs_install_fixture(tmp_path: Path) -> Iterator[Path]:
    with patch("dcs.installation.read_current_user_value") as mock:
        configure_registry_mock(mock, standalone_beta=tmp_path)
        yield tmp_path


@pytest.fixture(name="none_installed")
def none_installed_fixture() -> Iterator[None]:
    with patch("dcs.installation.read_current_user_value") as mock:
        configure_registry_mock(mock)
        yield


def test_get_dcs_install_directory_stable(stable_dcs_install: Path) -> None:
    assert get_dcs_install_directory() == f"{stable_dcs_install}\\"


def test_get_dcs_install_directory_beta(beta_dcs_install: Path) -> None:
    assert get_dcs_install_directory() == f"{beta_dcs_install}\\"


def test_get_dcs_install_directory_steam(steam_dcs_install: Path) -> None:
    assert get_dcs_install_directory() == f"{steam_dcs_install}\\"


def test_get_dcs_install_directory_not_installed(none_installed: None) -> None:
    assert get_dcs_install_directory() == ""


@patch("os.path.expanduser")
@patch("dcs.installation.get_dcs_install_directory")
def test_get_dcs_saved_games_directory_no_variant_file(
    mock_get_dcs_install_directory: Mock, mock_expanduser: Mock, tmp_path: Path
) -> None:
    home_dir = tmp_path / "home"

    mock_expanduser.return_value = str(home_dir)
    mock_get_dcs_install_directory.return_value = str(tmp_path)

    assert get_dcs_saved_games_directory() == str(home_dir / "Saved Games/DCS")


@patch("os.path.expanduser")
@patch("dcs.installation.get_dcs_install_directory")
def test_get_dcs_saved_games_directory_beta_variant(
    mock_get_dcs_install_directory: Mock, mock_expanduser: Mock, tmp_path: Path
) -> None:
    install_dir = tmp_path / "install/steamapps/common/DCSWorld"
    install_dir.mkdir(parents=True)
    home_dir = tmp_path / "home"

    (install_dir / "dcs_variant.txt").write_text("openbeta")

    mock_expanduser.return_value = str(home_dir)
    mock_get_dcs_install_directory.return_value = install_dir

    assert get_dcs_saved_games_directory() == str(home_dir / "Saved Games/DCS.openbeta")
