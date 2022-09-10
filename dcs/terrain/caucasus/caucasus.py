# flake8: noqa
import os

from dcs.terrain.terrain import Terrain, MapView, Graph
import dcs.mapping as mapping
from .airports import ALL_AIRPORTS
from .projection import PARAMETERS


class Caucasus(Terrain):
    center = {"lat": 43.69666, "long": 32.96}
    temperature = [
        (-4, 14),
        (-8, 14),
        (-6, 16),
        (0, 19),
        (1, 24),
        (8, 30),
        (12, 33),
        (12, 32),
        (10, 28),
        (2, 22),
        (-2, 14),
        (-4, 12)
    ]
    assert len(temperature) == 12

    def __init__(self):
        super().__init__(
            "Caucasus",
            PARAMETERS,
            bounds=mapping.Rectangle(380 * 1000, -560 * 1000, -600 * 1000, 1130 * 1000, self),
            map_view_default=MapView(mapping.Point(-255714.28571428, 680571.42857143, self), self, 1000000)
        )
        # caucasus center MGRS
        # 36TWQ9949898109
        self.bullseye_blue = {"x": -291014, "y": 617414}
        self.bullseye_red = {"x": 11557, "y": 371700}

        try:
            self.city_graph: Graph = Graph.from_pickle(os.path.join(os.path.dirname(__file__), 'citygraph.p'))
        except FileNotFoundError:
            pass

        self.airports = {a.name: a(self) for a in ALL_AIRPORTS}

        self.airports["Anapa-Vityazevo"].unit_zones.append(mapping.Rectangle(-5802.857142854, 242768.57142857,
                                                                   -7402.857142854, 244368.57142857, self))
        self.airports["Anapa-Vityazevo"].unit_zones.append(mapping.Rectangle(-4217.1428571397, 239325.71428572,
                                                                   -5417.1428571397, 240525.71428572, self))
        self.airports["Anapa-Vityazevo"].unit_zones.append(mapping.Rectangle(-5759.9999999969, 239132.85714286,
                                                                   -7159.9999999969, 240532.85714286, self))
        self.airports["Anapa-Vityazevo"].unit_zones.append(mapping.Rectangle(-3967.1428571397, 245318.57142857,
                                                                   -6767.1428571397, 248118.57142857, self))

        self.airports["Krasnodar-Center"].unit_zones.append(mapping.Rectangle(13360.857142856, 366714.28571429,
                                                                    12360.857142856, 367714.28571429, self))
        self.airports["Krasnodar-Center"].unit_zones.append(mapping.Rectangle(13375.142857142, 367717.14285714,
                                                                    12375.142857142, 368717.14285714, self))
        self.airports["Krasnodar-Center"].unit_zones.append(mapping.Rectangle(11072.285714285, 366687.14285714,
                                                                    10372.285714285, 367387.14285714, self))
        self.airports["Krasnodar-Center"].unit_zones.append(mapping.Rectangle(15490.857142856, 361865.71428571,
                                                                    12490.857142856, 364865.71428571, self))

        self.airports["Novorossiysk"].unit_zones.append(mapping.Rectangle(-39022.285714285, 277836.85714285,
                                                                -40122.285714285, 278936.85714285, self))
        self.airports["Novorossiysk"].unit_zones.append(mapping.Rectangle(-40290.857142857, 279953.99999999,
                                                                -40790.857142857, 280453.99999999, self))
        self.airports["Novorossiysk"].unit_zones.append(mapping.Rectangle(-40255.142857142, 276589.71428571,
                                                                -41155.142857142, 277489.71428571, self))

        self.airports["Krymsk"].unit_zones.append(mapping.Rectangle(-6292.8571428566, 295422.85714286,
                                                          -7292.8571428566, 296422.85714286, self))
        self.airports["Krymsk"].unit_zones.append(mapping.Rectangle(-5878.5714285709, 292315.71428571,
                                                          -6878.5714285709, 293315.71428571, self))
        self.airports["Krymsk"].unit_zones.append(mapping.Rectangle(-4885.7142857137, 293180,
                                                          -5885.7142857137, 294180, self))
        self.airports["Krymsk"].unit_zones.append(mapping.Rectangle(-5414.2857142852, 295651.42857143,
                                                          -6214.2857142852, 296451.42857143, self))

        self.airports["Maykop-Khanskaya"].unit_zones.append(mapping.Rectangle(-24574.285714285, 455938.57142857,
                                                                    -26574.285714285, 457938.57142857, self))
        self.airports["Maykop-Khanskaya"].unit_zones.append(mapping.Rectangle(-26888.571428571, 459010,
                                                                    -29088.571428571, 461210, self))
        self.airports["Maykop-Khanskaya"].unit_zones.append(mapping.Rectangle(-24917.142857142, 459945.71428572,
                                                                    -26717.142857142, 461745.71428572, self))
        self.airports["Maykop-Khanskaya"].unit_zones.append(mapping.Rectangle(-29138.57142857, 457451.42857144,
                                                                    -30738.57142857, 459051.42857144, self))

        self.airports["Gelendzhik"].unit_zones.append(mapping.Rectangle(-50072.857142857, 296894.28571429,
                                                              -50972.857142857, 297794.28571429, self))
        self.airports["Gelendzhik"].unit_zones.append(mapping.Rectangle(-49435.714285714, 296528.57142857,
                                                              -50135.714285714, 297228.57142857, self))
        self.airports["Gelendzhik"].unit_zones.append(mapping.Rectangle(-50470, 298271.42857143,
                                                              -51170, 298971.42857143, self))
        self.airports["Gelendzhik"].unit_zones.append(mapping.Rectangle(-48665.714285714, 297704.28571428,
                                                              -49265.714285714, 298304.28571428, self))

        self.airports["Krasnodar-Pashkovsky"].unit_zones.append(mapping.Rectangle(8105.7142857243, 388292.85714286,
                                                                        6705.7142857243, 389692.85714286, self))
        self.airports["Krasnodar-Pashkovsky"].unit_zones.append(mapping.Rectangle(7184.2857142957, 384857.14285715,
                                                                        6184.2857142957, 385857.14285715, self))
        self.airports["Krasnodar-Pashkovsky"].unit_zones.append(mapping.Rectangle(8848.5714285814, 386628.57142858,
                                                                        7948.571428581399, 387528.57142858, self))
        self.airports["Krasnodar-Pashkovsky"].unit_zones.append(mapping.Rectangle(9570.0000000098, 383164.28571429,
                                                                        8570.0000000098, 384164.28571429, self))

        self.airports["Sukhumi-Babushara"].unit_zones.append(mapping.Rectangle(-220484.28571428, 563282.85714286,
                                                                     -221084.28571428, 563882.85714286, self))
        self.airports["Sukhumi-Babushara"].unit_zones.append(mapping.Rectangle(-220081.42857143, 562380.00000001,
                                                                     -220681.42857143, 562980.00000001, self))
        self.airports["Sukhumi-Babushara"].unit_zones.append(mapping.Rectangle(-218804.28571429, 564057.14285715,
                                                                     -219404.28571429, 564657.14285715, self))
        self.airports["Sukhumi-Babushara"].unit_zones.append(mapping.Rectangle(-218895.71428571, 563268.57142858,
                                                                     -219495.71428571, 563868.57142858, self))
        self.airports["Sukhumi-Babushara"].unit_zones.append(mapping.Rectangle(-221415.71428571, 565074.28571429,
                                                                     -222015.71428571, 565674.28571429, self))

        self.airports["Gudauta"].unit_zones.append(mapping.Rectangle(-196705.71428572, 516900,
                                                           -197405.71428572, 517600, self))
        self.airports["Gudauta"].unit_zones.append(mapping.Rectangle(-195732.85714286, 514945.71428571,
                                                           -196332.85714286, 515545.71428571, self))
        self.airports["Gudauta"].unit_zones.append(mapping.Rectangle(-195075.71428572, 516880,
                                                           -195875.71428572, 517680, self))

        self.airports["Batumi"].unit_zones.append(mapping.Rectangle(-356160, 616688.00000003,
                                                          -356960, 617488.00000003, self))
        self.airports["Batumi"].unit_zones.append(mapping.Rectangle(-357551.42857143, 614990.85714289,
                                                          -358551.42857143, 615990.85714289, self))
        self.airports["Batumi"].unit_zones.append(mapping.Rectangle(-355574.28571429, 615740.85714289,
                                                          -356474.28571429, 616640.85714289, self))

        self.airports["Senaki-Kolkhi"].unit_zones.append(mapping.Rectangle(-281829.99999999, 646374.2857143,
                                                                 -282629.99999999, 647174.2857143, self))
        self.airports["Senaki-Kolkhi"].unit_zones.append(mapping.Rectangle(-280231.42857142, 645832.85714287,
                                                                 -280931.42857142, 646532.85714287, self))
        self.airports["Senaki-Kolkhi"].unit_zones.append(mapping.Rectangle(-282110, 645288.57142859,
                                                                 -282910, 646088.57142859, self))
        self.airports["Senaki-Kolkhi"].unit_zones.append(mapping.Rectangle(-281052.85714285, 648450.00000002,
                                                                 -281452.85714285, 648850.00000002, self))

        self.airports["Kobuleti"].unit_zones.append(mapping.Rectangle(-319184.85714285, 636121.14285715,
                                                            -320584.85714285, 637521.14285715, self))
        self.airports["Kobuleti"].unit_zones.append(mapping.Rectangle(-317053.42857142, 634509.71428572,
                                                            -317553.42857142, 635009.71428572, self))
        self.airports["Kobuleti"].unit_zones.append(mapping.Rectangle(-317776.28571428, 634158.28571429,
                                                            -318276.28571428, 634658.28571429, self))

        self.airports["Kutaisi"].unit_zones.append(mapping.Rectangle(-285691.42857142, 683870.00000001,
                                                           -286691.42857142, 684870.00000001, self))
        self.airports["Kutaisi"].unit_zones.append(mapping.Rectangle(-285131.42857142, 685257.14285716,
                                                           -286131.42857142, 686257.14285716, self))
        self.airports["Kutaisi"].unit_zones.append(mapping.Rectangle(-283062.85714285, 682065.71428573,
                                                           -283762.85714285, 682765.71428573, self))
        self.airports["Kutaisi"].unit_zones.append(mapping.Rectangle(-283252.85714285, 685130.00000001,
                                                           -283752.85714285, 685630.00000001, self))

        self.airports["Mineralnye Vody"].unit_zones.append(mapping.Rectangle(-50675.714285712, 706205.71428572,
                                                                   -51275.714285712, 706805.71428572, self))
        self.airports["Mineralnye Vody"].unit_zones.append(mapping.Rectangle(-52302.857142855, 704720,
                                                                   -53002.857142855, 705420, self))
        self.airports["Mineralnye Vody"].unit_zones.append(mapping.Rectangle(-51194.285714284, 701500,
                                                                   -52594.285714284, 702900, self))
        self.airports["Mineralnye Vody"].unit_zones.append(mapping.Rectangle(-48049.999999998, 706642.85714286,
                                                                   -48849.999999998, 707442.85714286, self))

        self.airports["Tbilisi-Lochini"].unit_zones.append(mapping.Rectangle(-315025.71428571, 894574.28571429,
                                                                   -316225.71428571, 895774.28571429, self))
        self.airports["Tbilisi-Lochini"].unit_zones.append(mapping.Rectangle(-316225.71428571, 896138.57142857,
                                                                   -317425.71428571, 897338.57142857, self))
        self.airports["Tbilisi-Lochini"].unit_zones.append(mapping.Rectangle(-314582.85714286, 897795.71428571,
                                                                   -315982.85714286, 899195.71428571, self))

        self.airports["Soganlug"].unit_zones.append(mapping.Rectangle(-318431.42857142, 894650.00000001,
                                                            -318931.42857142, 895150.00000001, self))
        self.airports["Soganlug"].unit_zones.append(mapping.Rectangle(-318949.99999999, 894894.28571429,
                                                            -319549.99999999, 895494.28571429, self))
        self.airports["Soganlug"].unit_zones.append(mapping.Rectangle(-318215.7142857, 897200.00000001,
                                                            -319215.7142857, 898200.00000001, self))

        self.airports["Vaziani"].unit_zones.append(mapping.Rectangle(-318605.71428571, 901664.28571429,
                                                           -319605.71428571, 902664.28571429, self))
        self.airports["Vaziani"].unit_zones.append(mapping.Rectangle(-319434.28571428, 902484.28571429,
                                                           -320434.28571428, 903484.28571429, self))
        self.airports["Vaziani"].unit_zones.append(mapping.Rectangle(-318435.71428571, 904565.71428572,
                                                           -319435.71428571, 905565.71428572, self))
        self.airports["Vaziani"].unit_zones.append(mapping.Rectangle(-316582.85714285, 903304.28571429,
                                                           -317582.85714285, 904304.28571429, self))

        self.airports["Sochi-Adler"].unit_zones.append(mapping.Rectangle(-164637.14285714, 461964.28571428,
                                                               -165237.14285714, 462564.28571428, self))
        self.airports["Sochi-Adler"].unit_zones.append(mapping.Rectangle(-162801.42857142, 460978.57142857,
                                                               -163601.42857142, 461778.57142857, self))
        self.airports["Sochi-Adler"].unit_zones.append(mapping.Rectangle(-165514.28571428, 461815.71428571,
                                                               -165914.28571428, 462215.71428571, self))
