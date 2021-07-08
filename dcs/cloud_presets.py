from enum import Enum, unique

from dcs.weather import CloudPreset


@unique
class Clouds(Enum):

    @staticmethod
    def from_name(name: str) -> "Clouds":
        return CLOUD_PRESETS[name]

    LightScattered1 = CloudPreset(
        name='Preset1',
        ui_name='Light Scattered 1',
        description='01 ##Few Scattered Clouds \nMETAR:FEW/SCT 7/8',
        min_base=840,
        max_base=4200,
    )

    Scattered5 = CloudPreset(
        name='Preset10',
        ui_name='Scattered 5',
        description='10 ##Two Layers Scattered Large Thick Clouds  \nMETAR:SCT/BKN 18/20 FEW36/38 FEW 40',
        min_base=1260,
        max_base=4200,
    )

    Scattered6 = CloudPreset(
        name='Preset11',
        ui_name='Scattered 6',
        description='11 ##Two Layers Scattered Large Clouds High Ceiling \nMETAR:BKN 18/20 BKN 32/33 FEW 41',
        min_base=2520,
        max_base=5460,
    )

    Scattered7 = CloudPreset(
        name='Preset12',
        ui_name='Scattered 7',
        description='12 ##Two Layers Scattered Large Clouds High Ceiling \nMETAR:BKN 12/14 SCT 22/23 FEW 41',
        min_base=1680,
        max_base=3360,
    )

    Broken1 = CloudPreset(
        name='Preset13',
        ui_name='Broken 1',
        description='13 ##Two Layers Broken Clouds \nMETAR:BKN 12/14 BKN 26/28 FEW 41',
        min_base=1680,
        max_base=3360,
    )

    Broken2 = CloudPreset(
        name='Preset14',
        ui_name='Broken 2',
        description='14 ##Broken Thick Low Layer with Few High Layer\nMETAR:BKN LYR 7/16 FEW 41',
        min_base=1680,
        max_base=3360,
    )

    Broken3 = CloudPreset(
        name='Preset15',
        ui_name='Broken 3',
        description='15 ##Two Layers Broken Large Clouds \nMETAR:SCT/BKN 14/18 BKN 24/27 FEW 40',
        min_base=840,
        max_base=5040,
    )

    Broken4 = CloudPreset(
        name='Preset16',
        ui_name='Broken 4',
        description='16 ##Two Layers Broken Large Clouds \nMETAR:BKN 14/18 BKN 28/30 FEW 40',
        min_base=1260,
        max_base=4200,
    )

    Broken5 = CloudPreset(
        name='Preset17',
        ui_name='Broken 5',
        description='17 ##Three Layers Broken/Overcast \nMETAR:BKN/OVC LYR 7/13 20/22 32/34',
        min_base=0,
        max_base=2520,
    )

    Broken6 = CloudPreset(
        name='Preset18',
        ui_name='Broken 6',
        description='18 ##Three Layers Broken/Overcast \nMETAR:BKN/OVC LYR 13/15 25/29 38/41',
        min_base=0,
        max_base=3780,
    )

    Broken7 = CloudPreset(
        name='Preset19',
        ui_name='Broken 7',
        description='19 ##Three Layers Overcast At Low Level \nMETAR:OVC 9/16 BKN/OVC LYR 23/24 31/33',
        min_base=0,
        max_base=2940,
    )

    LightScattered2 = CloudPreset(
        name='Preset2',
        ui_name='Light Scattered 2',
        description='02 ##Two Layers Few and Scattered \nMETAR:FEW/SCT 8/10 SCT 23/24',
        min_base=1260,
        max_base=2520,
    )

    Broken8 = CloudPreset(
        name='Preset20',
        ui_name='Broken 8',
        description='20 ##Three Layers Overcast Low Level \nMETAR:BKN/OVC 13/18 BKN 28/30 SCT FEW 38',
        min_base=0,
        max_base=3780,
    )

    Overcast1 = CloudPreset(
        name='Preset21',
        ui_name='Overcast 1',
        description='21 ##Overcast low level \nMETAR:BKN/OVC LYR 7/8 17/19',
        min_base=1260,
        max_base=4200,
    )

    Overcast2 = CloudPreset(
        name='Preset22',
        ui_name='Overcast 2',
        description='22 ##Overcast low Level \nMETAR:BKN LYR 7/10 17/20',
        min_base=420,
        max_base=4200,
    )

    Overcast3 = CloudPreset(
        name='Preset23',
        ui_name='Overcast 3',
        description='23 ##Three Layer Broken Low Level Scattered High \nMETAR:BKN LYR 11/14 18/25 SCT 32/35',
        min_base=840,
        max_base=3360,
    )

    Overcast4 = CloudPreset(
        name='Preset24',
        ui_name='Overcast 4',
        description='24 ##Three Layer Overcast \nMETAR:BKN/OVC 3/7 17/22 BKN 34',
        min_base=420,
        max_base=2520,
    )

    Overcast5 = CloudPreset(
        name='Preset25',
        ui_name='Overcast 5',
        description='25 ##Three Layer Overcast \nMETAR:OVC LYR 12/14 22/25 40/42',
        min_base=420,
        max_base=3360,
    )

    Overcast6 = CloudPreset(
        name='Preset26',
        ui_name='Overcast 6',
        description='26 ##Three Layer Overcast \nMETAR:OVC 9/15 BKN 23/25 SCT 32',
        min_base=420,
        max_base=2940,
    )

    Overcast7 = CloudPreset(
        name='Preset27',
        ui_name='Overcast 7',
        description='27 ##Three Layer Overcast \nMETAR:OVC 8/15 SCT/BKN 25/26 34/36',
        min_base=420,
        max_base=2520,
    )

    HighScattered1 = CloudPreset(
        name='Preset3',
        ui_name='High Scattered 1',
        description='03 ##Two Layer Scattered \nMETAR:SCT 8/9 FEW 21',
        min_base=840,
        max_base=2520,
    )

    HighScattered2 = CloudPreset(
        name='Preset4',
        ui_name='High Scattered 2',
        description='04 ##Two Layer Scattered \nMETAR:SCT 8/10 FEW/SCT 24/26',
        min_base=1260,
        max_base=2520,
    )

    Scattered1 = CloudPreset(
        name='Preset5',
        ui_name='Scattered 1',
        description='05 ##Three Layer High altitude Scattered \nMETAR:SCT 14/17 FEW 27/29 BKN 40',
        min_base=1260,
        max_base=4620,
    )

    Scattered2 = CloudPreset(
        name='Preset6',
        ui_name='Scattered 2',
        description='06 ##One Layer Scattered/Broken \nMETAR:SCT/BKN 8/10 FEW 40',
        min_base=1260,
        max_base=4200,
    )

    Scattered3 = CloudPreset(
        name='Preset7',
        ui_name='Scattered 3',
        description='07 ##Two Layer Scattered/Broken \nMETAR:BKN 7.5/12 SCT/BKN 21/23 SCT 40',
        min_base=1680,
        max_base=5040,
    )

    HighScattered3 = CloudPreset(
        name='Preset8',
        ui_name='High Scattered 3',
        description='08 ##Two Layer Scattered/Broken High Altitude \nMETAR:SCT/BKN 18/20 FEW 36/38 FEW 40',
        min_base=3780,
        max_base=5460,
    )

    Scattered4 = CloudPreset(
        name='Preset9',
        ui_name='Scattered 4',
        description='09 ##Two Layer Broken/Scattered \nMETAR:BKN 7.5/10 SCT 20/22 FEW41',
        min_base=1680,
        max_base=3780,
    )

    OvercastAndRain1 = CloudPreset(
        name='RainyPreset1',
        ui_name='Overcast And Rain 1',
        description='28 ##Overcast with Rain \nMETAR:VIS 3-5KM RA OVC 3/15 28/30 FEW 40',
        min_base=420,
        max_base=2940,
    )

    OvercastAndRain2 = CloudPreset(
        name='RainyPreset2',
        ui_name='Overcast And Rain 2',
        description='29 ##Overcast with Rain \nMETAR:VIS 1-5KM RA BKN/OVC 3/11 SCT 18/29 FEW 40',
        min_base=840,
        max_base=2520,
    )

    OvercastAndRain3 = CloudPreset(
        name='RainyPreset3',
        ui_name='Overcast And Rain 3',
        description='30 ##Overcast with Rain \nMETAR:VIS 3-5KM RA OVC LYR 6/18 19/21 SCT 34',
        min_base=840,
        max_base=2520,
    )


CLOUD_PRESETS = {
    'Preset1': Clouds.LightScattered1,
    'Preset10': Clouds.Scattered5,
    'Preset11': Clouds.Scattered6,
    'Preset12': Clouds.Scattered7,
    'Preset13': Clouds.Broken1,
    'Preset14': Clouds.Broken2,
    'Preset15': Clouds.Broken3,
    'Preset16': Clouds.Broken4,
    'Preset17': Clouds.Broken5,
    'Preset18': Clouds.Broken6,
    'Preset19': Clouds.Broken7,
    'Preset2': Clouds.LightScattered2,
    'Preset20': Clouds.Broken8,
    'Preset21': Clouds.Overcast1,
    'Preset22': Clouds.Overcast2,
    'Preset23': Clouds.Overcast3,
    'Preset24': Clouds.Overcast4,
    'Preset25': Clouds.Overcast5,
    'Preset26': Clouds.Overcast6,
    'Preset27': Clouds.Overcast7,
    'Preset3': Clouds.HighScattered1,
    'Preset4': Clouds.HighScattered2,
    'Preset5': Clouds.Scattered1,
    'Preset6': Clouds.Scattered2,
    'Preset7': Clouds.Scattered3,
    'Preset8': Clouds.HighScattered3,
    'Preset9': Clouds.Scattered4,
    'RainyPreset1': Clouds.OvercastAndRain1,
    'RainyPreset2': Clouds.OvercastAndRain2,
    'RainyPreset3': Clouds.OvercastAndRain3,
}
