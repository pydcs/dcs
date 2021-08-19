import dcs.lua as lua


class A10CPresets:
    def __init__(self):
        self.presets: dict[int, int] = {
            1: 305000000,
            2: 264000000,
            3: 265000000,
            4: 256000000,
            5: 254000000,
            6: 250000000,
            7: 270000000,
            8: 257000000,
            9: 255000000,
            10: 262000000,
            11: 259000000,
            12: 268000000,
            13: 269000000,
            14: 260000000,
            15: 263000000,
            16: 261000000,
            17: 267000000,
            18: 251000000,
            19: 253000000,
            20: 266000000,
        }

    def load_dict(self, data):
        presets = data.get("settings", {}).get("presets", {})
        for chan, freq in presets.items():
            self.presets[chan] = freq

    def set_preset(self, channel: int, frequency: float):
        freq_as_int = round(frequency * 10 ** 6)
        self.presets[channel] = freq_as_int

    def get_preset(self, channel: int) -> float:
        frequency = self.presets[channel]
        # TODO: Check if floating point precision is a problem
        freq_as_float = frequency / (10 ** 6)
        return freq_as_float

    def __str__(self):
        d = {
            # TODO: dials if needed?
            "presets": self.presets,
        }
        return lua.dumps(d, "settings", 1)


# Example data from UHF_RADIO/SETTINGS.lua in a miz file:

# -- These values overwrites the default settings for the A-10C, including hotstarts.
# -- To enable the server wide dials settings, remove the --
# settings=
# {
# 	--["dials"]=
# 	{
# 		["mode_dial"]=0, -- 0=OFF, 1=MAIN, 2=BOTH, 3=ADF
# 		["manual_frequency"]=305000000, -- Overwrites the value set in the ME. Default=251000000
# 		["selection_dial"]=0, -- 1=MNL, 2=PRESET, 3=GRD
# 		["channel_dial"]=0, -- See the presets below. 0=preset 1, 1=preset 2, etc
# 	},
# 	["presets"]=
# 	{
# 		[1]=305000000,
# 		[2]=264000000,
# 		[3]=265000000,
# 		[4]=256000000,
# 		[5]=254000000,
# 		[6]=250000000,
# 		[7]=270000000,
# 		[8]=257000000,
# 		[9]=255000000,
# 		[10]=262000000,
# 		[11]=259000000,
# 		[12]=268000000,
# 		[13]=269000000,
# 		[14]=260000000,
# 		[15]=263000000,
# 		[16]=261000000,
# 		[17]=267000000,
# 		[18]=251000000,
# 		[19]=253000000,
# 		[20]=266000000,
# 	},
# }
