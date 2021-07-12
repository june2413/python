# 단위 변환 함수
def convertLength(unit):
    units = {}

    units['mm'] = unit
    units['cm'] = unit * 0.1
    units['m'] = unit * 0.001
    units['inch'] = unit * 0.03937
    units['feet'] = unit * 0.003281

    return units

def printUnits(units):
    for k, v in units.items():
        print(f"{k} -> {v}")