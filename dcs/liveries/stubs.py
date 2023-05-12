from .liveryscanner import LiveryScanner, safe_name


def generate_stub() -> None:
    if __name__ != "__main__":
        print("Stub should not be generated externally!")
        return
    LiveryScanner()  # initialize in case that hasn't happened yet.
    with open("liveries_scanner.pyi", "w", encoding="utf8") as file:
        with open(
            "stub templates/liveries_scanner.pyi", "r", encoding="utf8"
        ) as template:
            file.write(template.read())
        for unit in LiveryScanner.map:
            file.write(f"\n    class {safe_name(unit)}(LiverySet):\n")
            safe_value = unit.replace("'", "\\'").replace('"', '"')
            file.write(f"        unit_livery_id = '{safe_value}'\n\n")
            for livery in sorted(LiveryScanner.map[unit]):
                file.write(f"        {safe_name(livery.id)}: Livery\n")


if __name__ == "__main__":
    generate_stub()  # generates the stub file for auto-completion

    # from planes import FA_18C_hornet, F_16C_50, F_14B, F_15E, A_10C_2, Liveries
    # # for some reason 'Liveries' in the current scope is a different object
    #
    # f18 = FA_18C_hornet()
    # print(f18.livery_name, sorted(f18.Liveries))
    # print(f18.default_livery("CAN"))
    # print(f18.default_livery("ISR"))
    # print(f18.default_livery("USA"))
    #
    # f14 = F_14B()
    # print(f14.livery_name, sorted(f14.Liveries))
    # print(f14.default_livery("USA"))
    # print(f14.default_livery("IRN"))
    # print(f14.default_livery("GRC"))
    # print(f14.default_livery("POL"))
    #
    # f15 = F_15E()
    # print(f15.livery_name, sorted(f15.Liveries))
    # print(f15.default_livery("USA"))
    # print(f15.default_livery("ISR"))
    # print(f15.default_livery("GRC"))
    # print(f15.default_livery("POL"))
    #
    # a10c2 = A_10C_2()
    # print(a10c2.livery_name, sorted(a10c2.Liveries))
    # print(a10c2.default_livery("USA"))
    # print(a10c2.default_livery("ISR"))
    # print(a10c2.default_livery("GRC"))
    # print(a10c2.default_livery("POL"))
    #
    # f16 = F_16C_50()
    # print(f16.livery_name, sorted(f16.Liveries))
    # print(f16.default_livery("USA"))
    # print(f16.default_livery("ISR"))
    # print(f16.default_livery("GRC"))
    # print(f16.default_livery("POL"))
    #
    # from helicopters import AH_64D_BLK_II
    # ah64 = AH_64D_BLK_II()
    # print(ah64.livery_name, sorted(ah64.Liveries))
    # print(ah64.default_livery("USA"))
    # print(ah64.default_livery("ISR"))
    #
    # print(Liveries.A_10A)
    # print(Liveries.F_16C_50.x14th_Fighter_Squadron)
    # print(Liveries.F_16C_50.x14th_Fighter_Squadron.order)
    # print(Liveries.F_16C_50.x14th_Fighter_Squadron.countries)
    # print(Liveries.map[Liveries.LEOPARD_2.unit_livery_id])
    #
    # from dcs.liveries_scanner import Livery
    # tester = Livery("Test_ID", "___TEST NAME___", 0, None)
    # Liveries.AH_64D_BLK_II.add(tester)
    # Liveries.AH_64D_BLK_II.add(Livery("Test_ID", "___TEST NAME___", 0, None))
    # print(Liveries.AH_64D_BLK_II)
    # print()
    # for livery in Liveries.LEOPARD_2:
    #     print(livery.id, livery.name, livery.order, livery.countries)
    # print()
    # for livery in Liveries.FA_18C_HORNET:
    #     print(livery.id, livery.name, livery.order, livery.countries)

    # skins = Liveries()
    # for u in skins:
    #     print(u)
    #     for liv in sorted(skins[u]):
    #         print("\t", liv, liv.countries)
