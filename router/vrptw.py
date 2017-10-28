import sys
import random
sys.path.append("/usr/src/app/py-ga-VRPTW")
from gavrptw.core import gaVRPTW

def vrptw_route(input_json):
    random.seed(64)

    instName = 'input'

    unitCost = 8.0
    initCost = 100.0
    waitCost = 1.0
    delayCost = 1.5

    indSize = 2
    popSize = 400
    cxPb = 0.85
    mutPb = 0.02
    NGen = 300

    exportCSV = True

    return gaVRPTW(
        instName=instName,
        unitCost=unitCost,
        initCost=initCost,
        waitCost=waitCost,
        delayCost=delayCost,
        indSize=indSize,
        popSize=popSize,
        cxPb=cxPb,
        mutPb=mutPb,
        NGen=NGen,
        exportCSV=exportCSV
    )
