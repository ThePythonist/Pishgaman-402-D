nomarat = {
    "riazi1": 14,
    "zaban": 20,
    "mabani computer": 20,
    "madar manteghi": 16,
    "andishe eslami": 7,
    "assembly": 10
}


def ghaboli(dars):
    if nomarat[dars] >= 10:
        print(dars, "Pass shode ast")
    else:
        print(dars, "Rad shode ast")


def moadel(doros):
    avg = sum(doros) / len(doros)


# ---------------------------------------------

for nomre in nomarat:
    ghaboli(nomre)

moadel(nomarat.values())
