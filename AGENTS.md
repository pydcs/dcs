# AGENTS.md

Guidance for AI coding agents (and humans) working in this repository.

## Project

**pydcs** (`dcs` package): a Python framework to create, load, edit and save mission files (`.miz`) for
the flight simulator *DCS World*. A `.miz` is a zip archive with Lua tables (`mission`, `options`,
`warehouses`, `l10n/DEFAULT/dictionary`, `mapResource`, …) plus resources. License: LGPLv3.
Package metadata and version live in `pyproject.toml` (setuptools backend, no `setup.py`).

## Setup & commands

Only runtime dependency is `pyproj` (`requirements.txt`). Use a virtualenv (`venv/` is gitignored):

```sh
python3 -m venv venv
./venv/bin/pip install -r requirements.txt mypy flake8 pytest
```

CI (`.github/workflows/pythonpackage.yml`, runs on **Windows and Linux**, Python 3.11–3.15) does exactly this —
run all three before considering a change done:

```sh
mypy dcs                                                        # type check (must be clean)
flake8 .                                                        # lint, config in setup.cfg
flake8 . --isolated --count --select=E9,F63,F7,F82 --show-source --statistics  # syntax check of excluded files
pytest                                                          # tests/ and dcs/lua/test_parse.py
```

- Single test: `pytest tests/test_mission.py::BasicTests::test_basic_mission`
- Tests use paths relative to the repo root (e.g. `tests/missions/*.miz` as input, `missions/` as output
  dir — gitignored), so run pytest from the repo root.
- The suite must pass on Windows and Linux. Use `os.path` / `pathlib` instead of hard-coded `\\`
  separators. Tests for genuinely Windows-only behavior (e.g. the `ansi` codec, Steam library parsing)
  are gated with `@pytest.mark.skipif(sys.platform != "win32", ...)`.
- Packaging: `make build` (`uv build`, sdist + wheel into `dist/`; `python -m build` works too),
  `make upload` (twine, credentials from `~/.pypirc`). Packages are auto-discovered (`dcs*`); non-Python
  files to ship must be listed under `[tool.setuptools.package-data]` in `pyproject.toml`. A separate CI
  job (`package`, Linux) runs `uv build`, `twine check --strict` and a smoke test of the installed wheel.

## Code style

- flake8 with max line length **127**, `max-complexity` 10 (C901 ignored). Generated data files, `tests/`,
  `tools/` and `doc/` are excluded from flake8 (see `setup.cfg`).
- The package ships `py.typed`; new/changed code in `dcs/` should be type annotated and pass `mypy dcs`.
- Commit messages: short imperative summary line (e.g. "Fix TriggerZoneQuadPoint argument forwarding to
  parent __init__"); data refreshes are titled "DCS <version> export".

## Architecture

- `dcs/mission.py` — `Mission` is the entry point: `Mission(terrain)`, `load_file()`, `save()`, and
  helpers to add groups/flights (`flight_group_inflight`, `awacs_flight`, `refuel_flight`, …).
  Holds coalitions, countries, triggers, weather, translations, drawings, warehouses, etc.
- **Load/save pattern**: most model classes implement `load_from_dict(d)` / `create_from_dict(...)` to
  read the parsed Lua table and `dict()` to produce it again. Round-tripping a mission without changes
  must not lose data — when adding fields, implement both directions and add a load/save test.
- `dcs/lua/` — own Lua table parser (`parse.loads`) and serializer (`serialize.dumps`) used for all
  `.miz` content. Serialization key order matters (ints numerically, then strings alphabetically).
- `dcs/translation.py` — `Translation`/`String`/`ResourceKey`: localized strings (`DictKey_*`) and
  resource files embedded in the `.miz`.
- `dcs/country.py`, `dcs/coalition.py`, `dcs/unitgroup.py`, `dcs/unit.py`, `dcs/flyingunit.py`,
  `dcs/point.py` — the object model of countries → groups → units / waypoints.
- `dcs/task.py`, `dcs/action.py`, `dcs/condition.py`, `dcs/triggers.py`, `dcs/goals.py` — waypoint
  tasks/commands/options and the trigger system (rules, conditions, actions, trigger zones).
- `dcs/unittype.py` — base classes (`FlyingType`, `VehicleType`, `ShipType`, `StaticType`) for unit
  type definitions; `dcs/payloads.py` and `dcs/liveries/` read payloads and liveries from the user's
  DCS installation (`dcs/installation.py`, `dcs/winreg.py` — degrade gracefully off Windows).
- `dcs/terrain/` — `terrain.py` defines `Terrain`, `Airport`, `Runway`, `ParkingSlot`, `Warehouse`,
  `Graph`; one subpackage per map (`caucasus`, `nevada`, `normandy`, `persiangulf`, `thechannel`,
  `syria`, `marianaislands`, `falklands`, `sinai`, `kola`, `germany`, `afghanistan`), each with
  `<map>.py` (the `Terrain` subclass incl. bounds, projection, `utc_offset`), `airports.py` (generated
  airport data) and `projection.py`. `dcs/mapping.py` handles points, vectors and lat/lon conversion via `pyproj`.
- `dcs/drawing/` — mission editor drawings (layers, lines, polygons, icons, text boxes).
- `dcs/scripts/` — example random-mission generators installed as console scripts (`dcs_random`,
  `dcs_dogfight_wwii`, `dcs_oil_convoy`).

## Generated files — don't hand-edit

These are produced from a running DCS installation and get overwritten on the next export:

- `dcs/planes.py`, `dcs/helicopters.py`, `dcs/vehicles.py`, `dcs/ships.py`, `dcs/statics.py`,
  `dcs/weapons_data.py`, `dcs/countries.py` — generated by `tools/pydcs_export.lua` (run inside the DCS
  mission editor). Fix the generator instead, and keep generated diffs out of unrelated changes.
- `dcs/terrain/*/airports.py` — generated via `tools/airport_import.py` (instructions in its docstring).
- `dcs/cloud_presets.py` — from `tools/weather_import.py`; projections from
  `tools/export_map_projection.py`.

These files are huge (`planes.py`, `countries.py` are ~40k lines) — search them, don't read them whole.

## Adding a new terrain

Add the subpackage (with `__init__.py`) under `dcs/terrain/` and export it in `dcs/terrain/__init__.py`;
packaging picks it up automatically. If the generated airport file needs it, add an `E126`
per-file-ignore in `setup.cfg`. Add a test in `tests/test_terrain.py`.

## Other directories

- `tests/` — pytest/unittest tests; sample missions in `tests/missions/` and `tests/*.miz`.
- `tools/` — data-export/import helpers and dev utilities (`missiondiff.py` diffs two `.miz` files).
- `doc/` — Sphinx docs (published on readthedocs).
