import json

filename = '/home/iyanu/Documents/SurveyApp/project/models/id.json' 

with open(filename, 'r') as f:
    index = json.load(f)


def getUID():
    intId = index.get('UD') + 1
    strId = str(intId).zfill(6)
    id = 'UD{}'.format(strId)

    index['UD'] = intId
    with open(filename, 'w') as wfile:
        json.dump(index, wfile, indent=2)
    return id


def getSID():
    intId = index.get('SD') + 1
    strId = str(intId).zfill(6)
    id = 'SD{}'.format(strId)

    index['SD'] = intId
    with open(filename, 'w') as wfile:
        json.dump(index, wfile, indent=2)
    return id


def getRID():
    intId = index.get('RD') + 1
    strId = str(intId).zfill(6)
    id = 'RD{}'.format(strId)

    index['RD'] = intId
    with open(filename, 'w') as wfile:
        json.dump(index, wfile, indent=2)
    return id
