"""Generates resources/dcs/beacons.json from the DCS installation.

DCS has a clouds.lua file that defines all the cloud presets introduced in DCS 2.7.
Example below. The only values we need for serialization are the names of the presets
and their min/max preset altitudes, but the names might also be useful to clients.
Translation of names and descriptions are not handled.

clouds =
{
	presets =
	{
		Preset1 =
		{
			visibleInGUI = true,
			readableName = '01 ##'.. _('Few Scattered Clouds \nMETAR:FEW/SCT 7/8'),
			readableNameShort = _('Light Scattered 1'),
			thumbnailName = 'Bazar/Effects/Clouds/Thumbnails/cloud_1.png',
			levelMap = 'bazar/effects/clouds/cloudsMap01.png',
			detailNoiseMapSize = 8500.00,
			precipitationPower = -1.00,
			presetAltMin = 840.00,
			presetAltMax = 4200.00,
			layers = {
				{
					altitudeMin = 2520,
					altitudeMax = 3780,
					tile = 9.024,
					shapeFactor = 0.015,
					density = 0.396,
					densityGrad = 0.622,
					coverage = 0.359,
					noiseFreq = 0.384,
					noiseBlur = 1.125,
					coverageMapFactor = 0.00,
					coverageMapUVOffsetX = 0.00,
					coverageMapUVOffsetY = 0.00,
				},
				{
					altitudeMin = 5040,
					altitudeMax = 6300,
					tile = 5.104,
					shapeFactor = 0.132,
					density = 0.410,
					densityGrad = 1.032,
					coverage = 0.308,
					noiseFreq = 0.813,
					noiseBlur = 1.500,
					coverageMapFactor = 0.00,
					coverageMapUVOffsetX = 0.00,
					coverageMapUVOffsetY = 0.00,
				},
				{
					altitudeMin = 10500,
					altitudeMax = 12180,
					tile = 0.880,
					shapeFactor = 0.201,
					density = 0.000,
					densityGrad = 2.000,
					coverage = 0.000,
					noiseFreq = 3.000,
					noiseBlur = 1.500,
					coverageMapFactor = 0.00,
					coverageMapUVOffsetX = 0.00,
					coverageMapUVOffsetY = 0.00,
				},
			}
		},
        ...
"""
import argparse
from contextlib import contextmanager
import dataclasses
import logging

try:
    import lupa
except ImportError as ex:
    raise RuntimeError(
        "Run `pip install lupa` to use this tool. It is not included in "
        "requirements.txt since most users will not need this dependency."
    ) from ex

from pathlib import Path
import operator
import os
import textwrap
from typing import Dict, Iterable, Union

from dcs.weather import CloudPreset

THIS_DIR = Path(__file__).parent.resolve()
SRC_DIR = THIS_DIR.parent
EXPORT_PATH = SRC_DIR / "dcs/cloud_presets.py"


@contextmanager
def cd(path: Path):
    cwd = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(cwd)


def cloud_presets(dcs_path: Path) -> Iterable[CloudPreset]:
    clouds_lua = dcs_path / "Config/Effects/clouds.lua"
    logging.info(f"Loading cloud presets from {clouds_lua}")

    with cd(dcs_path):
        lua = lupa.LuaRuntime()

        # Define the translation function to a no-op because we don't need it.
        lua.execute(
            textwrap.dedent(
                """\
                function _(key)
                    return key
                end

                """
            )
        )

        lua.execute(clouds_lua.read_text())

    for name, data in lua.eval("clouds['presets']").items():
        if not data["visibleInGUI"]:
            # Not something choosable in the ME, so skip it.
            continue

        yield CloudPreset(
            name,
            ui_name=data["readableNameShort"],
            description=data["readableName"],
            min_base=data["presetAltMin"],
            max_base=data["presetAltMax"],
        )


class Importer:
    """Imports cloud presets."""

    def __init__(self, dcs_path: Path, export_path: Path) -> None:
        self.dcs_path = dcs_path
        self.export_path = export_path

    def run(self) -> None:
        """Exports the beacons for each available terrain mod."""
        self.export_path.parent.mkdir(parents=True, exist_ok=True)

        with self.export_path.open("w") as output:
            output.write(textwrap.dedent(
                """\
                from enum import Enum, unique

                from dcs.weather import CloudPreset


                @unique
                class Clouds(Enum):

                    @staticmethod
                    def from_name(name: str) -> "CloudPreset":
                        return CLOUD_PRESETS[name]

                """
            ))

            presets = sorted(cloud_presets(self.dcs_path),
                             key=operator.attrgetter("name"))
            names = {}
            for preset in presets:
                name = preset.ui_name.replace(" ", "")
                names[preset.name] = name
                preset_src = textwrap.dedent(
                    f"""\
                    {name} = CloudPreset(
                        name={repr(preset.name)},
                        ui_name={repr(preset.ui_name)},
                        description={repr(preset.description)},
                        min_base={repr(preset.min_base)},
                        max_base={repr(preset.max_base)},
                    )

                    """
                )
                output.write(textwrap.indent(preset_src, "    "))

            output.write("\nCLOUD_PRESETS = {\n")
            for name in names:
                output.write(f"    {repr(name)}: Clouds.{names[name]},\n")
            output.write("}\n")


def parse_args() -> argparse.Namespace:
    """Parses and returns command line arguments."""
    parser = argparse.ArgumentParser()

    def resolved_path(val: str) -> Path:
        """Returns the given string as a fully resolved Path."""
        return Path(val).resolve()

    parser.add_argument(
        "--export-to",
        type=resolved_path,
        default=EXPORT_PATH,
        help="Output directory for generated JSON files.",
    )

    parser.add_argument(
        "dcs_path",
        metavar="DCS_PATH",
        type=resolved_path,
        help="Path to DCS installation.",
    )

    return parser.parse_args()


def main() -> None:
    """Program entry point."""
    logging.basicConfig(level=logging.DEBUG)
    args = parse_args()
    Importer(args.dcs_path, args.export_to).run()


if __name__ == "__main__":
    main()
