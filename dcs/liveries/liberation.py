import json
import os
from typing import Tuple


def read_liberation_preferences() -> Tuple[str, str]:
    # TODO: Remove Liberation-specific behavior.
    # This is only necessary because it doesn't appear to be possible to 100% reliably
    # guess the DCS install or user directory. Liberation solves this by just asking the
    # user on first run. That's a problem for every pydcs user, not just Liberation.
    # This should go away in favor of making dcs.installation *guess* at the paths, but
    # with an API to override from the app side (similar to PayloadDirectories APIs).
    install = ""
    saved_games = ""
    pref_path = os.path.join(
        os.path.expanduser("~"), "AppData", "Local", "DCSLiberation"
    )
    pref_path = os.path.join(pref_path, "liberation_preferences.json")
    if os.path.exists(pref_path):
        with open(pref_path, "r") as file:
            try:
                json_dict = json.load(file)
                if "dcs_install_dir" in json_dict:
                    install = json_dict["dcs_install_dir"]
                if "saved_game_dir" in json_dict:
                    saved_games = json_dict["saved_game_dir"]
            except (KeyError, ValueError):
                # ValueError for decode errors (if the file is corrupted), KeyError in
                # case the format isn't what we expect.
                return "", ""
    return install, saved_games
