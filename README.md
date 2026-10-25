# python dcs mission framework

pydcs is a python framework for creating and editing mission files
from digital combat simulator.

Possible use cases are:

 * assisting mission creators
 * random mission creation
 * write an external mission editor on top of it
 * data export from existing missions
 * ...

## Sample

    import dcs
    m = dcs.Mission()

    batumi = m.terrain.batumi()
    batumi.set_blue()

    usa = m.country("USA")
    m.awacs_flight(
       usa, "AWACS", dcs.planes.E_3A,
       batumi, dcs.Point(batumi.position.x + 20000, batumi.position.y + 80000),
       race_distance=120 * 1000, heading=90)

    m.save("sample.miz")

This code generates a mission with a AWACS flight starting cold from batumi.

## Random mission scripts

pydcs comes with 2 proof of concept scripts:

### dcs_random

This script generates a random training mission on the Nevada map: player flight(s) for the
A-10C, M-2000C, Ka-50, AV-8B or F/A-18C at Nellis, Creech or Groom Lake, with AWACS, tankers and
civil air traffic around them.

For options see the script help with `dcs_random --help`

### dcs_dogfight_wwii

This script randomly generates WWII dogfights with a given number of planes near a random airport.
For options also see the script help `dcs_dogfight_wwii --help`

###

## Install

    pip install pydcs

## Documentation

The current documentation can be found [here](http://dcs.readthedocs.org/en/latest)

## TODO

 * Failures
 * More/better documentation
