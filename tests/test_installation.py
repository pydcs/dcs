import sys

try:
    import winreg
except ImportError:
    pass
from pathlib import Path
from unittest.mock import Mock, call, patch

import pytest

from dcs.installation import (
    DCS_BETA_REGISTRY_KEY_NAME,
    DCS_STABLE_REGISTRY_KEY_NAME,
    STEAM_REGISTRY_KEY_NAME,
    get_dcs_install_directory,
    get_dcs_saved_games_directory,
    is_using_dcs_standalone_edition,
    is_using_dcs_steam_edition,
)

pytestmark = pytest.mark.skipif(
    sys.platform != "win32", reason="dcs.installation is windows only"
)


@patch("winreg.CloseKey")
@patch("winreg.QueryValueEx")
@patch("winreg.OpenKey")
def test_is_using_dcs_steam_edition(
    mock_openkey: Mock, mock_queryvalueex: Mock, mock_closekey: Mock
) -> None:
    mock_openkey.return_value = "key"
    mock_queryvalueex.return_value = (1, 4)

    assert is_using_dcs_steam_edition()
    mock_openkey.assert_called_once_with(
        winreg.HKEY_CURRENT_USER, STEAM_REGISTRY_KEY_NAME
    )
    mock_queryvalueex.assert_called_once_with("key", "Installed")
    mock_closekey.assert_called_once_with("key")


@patch("winreg.CloseKey")
@patch("winreg.OpenKey")
def test_is_using_dcs_steam_edition_no_key(
    mock_openkey: Mock, mock_closekey: Mock
) -> None:
    mock_openkey.side_effect = FileNotFoundError

    assert not is_using_dcs_steam_edition()
    mock_openkey.assert_called_once_with(
        winreg.HKEY_CURRENT_USER, STEAM_REGISTRY_KEY_NAME
    )
    mock_closekey.assert_not_called()


@pytest.mark.xfail(strict=True)  # Does not close the key.
@patch("winreg.CloseKey")
@patch("winreg.QueryValueEx")
@patch("winreg.OpenKey")
def test_is_using_dcs_steam_edition_no_value(
    mock_openkey: Mock, mock_queryvalueex: Mock, mock_closekey: Mock
) -> None:
    mock_openkey.return_value = "key"
    mock_queryvalueex.side_effect = FileNotFoundError

    assert not is_using_dcs_steam_edition()
    mock_openkey.assert_called_once_with(
        winreg.HKEY_CURRENT_USER, STEAM_REGISTRY_KEY_NAME
    )
    mock_queryvalueex.assert_called_once_with("key", "Installed")
    mock_closekey.assert_called_once_with("key")


@patch("winreg.CloseKey")
@patch("winreg.QueryValueEx")
@patch("winreg.OpenKey")
def test_is_using_dcs_steam_edition_not_installed(
    mock_openkey: Mock, mock_queryvalueex: Mock, mock_closekey: Mock
) -> None:
    mock_openkey.return_value = "key"
    mock_queryvalueex.return_value = (0, 0)

    assert not is_using_dcs_steam_edition()
    mock_openkey.assert_called_once_with(
        winreg.HKEY_CURRENT_USER, STEAM_REGISTRY_KEY_NAME
    )
    mock_queryvalueex.assert_called_once_with("key", "Installed")
    mock_closekey.assert_called_once_with("key")


@patch("winreg.CloseKey")
@patch("winreg.OpenKey")
def test_is_using_dcs_standalone_edition_stable(
    mock_openkey: Mock, mock_closekey: Mock
) -> None:
    def stable_installed(key_type: int, name: str) -> str:
        if (
            key_type == winreg.HKEY_CURRENT_USER
            and name == DCS_STABLE_REGISTRY_KEY_NAME
        ):
            return "key"
        raise FileNotFoundError

    mock_openkey.side_effect = stable_installed

    assert is_using_dcs_standalone_edition()
    mock_openkey.assert_has_calls(
        [call(winreg.HKEY_CURRENT_USER, DCS_STABLE_REGISTRY_KEY_NAME)]
    )
    mock_closekey.assert_called_once_with("key")


@patch("winreg.CloseKey")
@patch("winreg.OpenKey")
def test_is_using_dcs_standalone_edition_beta(
    mock_openkey: Mock, mock_closekey: Mock
) -> None:
    def stable_installed(key_type: int, name: str) -> str:
        if key_type == winreg.HKEY_CURRENT_USER and name == DCS_BETA_REGISTRY_KEY_NAME:
            return "key"
        raise FileNotFoundError

    mock_openkey.side_effect = stable_installed

    assert is_using_dcs_standalone_edition()
    mock_openkey.assert_has_calls(
        [call(winreg.HKEY_CURRENT_USER, DCS_BETA_REGISTRY_KEY_NAME)]
    )
    mock_closekey.assert_called_once_with("key")


@patch("winreg.CloseKey")
@patch("winreg.OpenKey")
def test_is_using_dcs_standalone_not_installed(
    mock_openkey: Mock, mock_closekey: Mock
) -> None:
    mock_openkey.side_effect = FileNotFoundError

    assert not is_using_dcs_standalone_edition()
    mock_openkey.assert_has_calls(
        [
            call(winreg.HKEY_CURRENT_USER, DCS_STABLE_REGISTRY_KEY_NAME),
            call(winreg.HKEY_CURRENT_USER, DCS_BETA_REGISTRY_KEY_NAME),
        ],
        any_order=True,
    )
    mock_closekey.assert_not_called()


@patch("dcs.installation.is_using_dcs_steam_edition")
@patch("dcs.installation.is_using_dcs_standalone_edition")
@patch("winreg.CloseKey")
@patch("winreg.QueryValueEx")
@patch("winreg.OpenKey")
def test_get_dcs_install_directory_stable(
    mock_openkey: Mock,
    mock_queryvalueex: Mock,
    mock_closekey: Mock,
    mock_standalone_edition: Mock,
    mock_steam_edition: Mock,
) -> None:
    def stable_installed(key_type: int, name: str) -> str:
        if (
            key_type == winreg.HKEY_CURRENT_USER
            and name == DCS_STABLE_REGISTRY_KEY_NAME
        ):
            return "key"
        raise FileNotFoundError

    mock_openkey.side_effect = stable_installed
    mock_queryvalueex.return_value = ("path",)
    mock_standalone_edition.return_value = True
    mock_steam_edition.return_value = False

    assert get_dcs_install_directory() == "path\\"

    mock_queryvalueex.assert_called_once_with("key", "Path")
    mock_closekey.assert_called_once_with("key")


@patch("dcs.installation.is_using_dcs_steam_edition")
@patch("dcs.installation.is_using_dcs_standalone_edition")
@patch("winreg.CloseKey")
@patch("winreg.QueryValueEx")
@patch("winreg.OpenKey")
def test_get_dcs_install_directory_beta(
    mock_openkey: Mock,
    mock_queryvalueex: Mock,
    mock_closekey: Mock,
    mock_standalone_edition: Mock,
    mock_steam_edition: Mock,
) -> None:
    def stable_installed(key_type: int, name: str) -> str:
        if key_type == winreg.HKEY_CURRENT_USER and name == DCS_BETA_REGISTRY_KEY_NAME:
            return "key"
        raise FileNotFoundError

    mock_openkey.side_effect = stable_installed
    mock_queryvalueex.return_value = ("path",)
    mock_standalone_edition.return_value = True
    mock_steam_edition.return_value = False

    assert get_dcs_install_directory() == "path\\"

    mock_queryvalueex.assert_called_once_with("key", "Path")
    mock_closekey.assert_called_once_with("key")


@patch("dcs.installation._get_steam_library_folders")
@patch("dcs.installation.is_using_dcs_steam_edition")
@patch("dcs.installation.is_using_dcs_standalone_edition")
def test_get_dcs_install_directory_steam(
    mock_standalone_edition: Mock,
    mock_steam_edition: Mock,
    mock_get_steam_library_folders: Mock,
    tmp_path: Path,
) -> None:
    install_dir = tmp_path / "steamapps/common/DCSWorld"
    install_dir.mkdir(parents=True)

    mock_standalone_edition.return_value = False
    mock_steam_edition.return_value = True
    mock_get_steam_library_folders.return_value = ["foo", str(tmp_path), "bar"]

    assert get_dcs_install_directory() == f"{install_dir}\\"


@patch("dcs.installation.is_using_dcs_steam_edition")
@patch("dcs.installation.is_using_dcs_standalone_edition")
def test_get_dcs_install_directory_not_installed(
    mock_standalone_edition: Mock,
    mock_steam_edition: Mock,
) -> None:
    mock_standalone_edition.return_value = False
    mock_steam_edition.return_value = False

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
