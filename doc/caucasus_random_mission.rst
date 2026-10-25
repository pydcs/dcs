Random mission script
=====================

pydcs delivers a small random mission creator script, installed as ``dcs_random``.
It generates a random training mission on the Nevada map.
This script was intended to show features of the framework and is also a little testbed.

It is invoked by the commandline with the following arguments::

 usage: dcs_random [-h] [-a {A-10C,M-2000C,Ka-50,AV8BNA,FA-18C_hornet}]
                   [-p PLAYERCOUNT] [-s {inflight,runway,warm,cold}]
                   [-d {random,day,night,dusk,dawn,noon}]
                   [-w {dynamic,dyncyclone,dynanti,dynone,clear}] [-u]
                   [--show-stats] [-o OUTPUT]

 Nevada random training mission generator

 options:
   -h, --help            show this help message and exit
   -a, --aircrafttype {A-10C,M-2000C,Ka-50,AV8BNA,FA-18C_hornet}
                         Player aircraft type
   -p, --playercount PLAYERCOUNT
   -s, --start {inflight,runway,warm,cold}
   -d, --daytime {random,day,night,dusk,dawn,noon}
   -w, --weather {dynamic,dyncyclone,dynanti,dynone,clear}
   -u, --unhide          Show enemy pre mission
   --show-stats          Show generated missions stats
   -o, --output OUTPUT   Name and path of the generated mission
