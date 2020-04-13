import pandas as pd

walsData = pd.read_csv('language.csv')


def findSeries(header):
    for series in walsData:
        if header in str(walsData[series]):
            return walsData[series]
    assert False, ('Searched for an invalid series.')


def findSeriesPair(header1, header2, removeNullAnswers):
    frame = {}
    for series in walsData:
        if (header1 in str(walsData[series])):
            frame[header1] = walsData[series]
        elif (header2 in str(walsData[series])):
            frame[header2] = walsData[series]
    df = pd.DataFrame(frame)
    if removeNullAnswers:
        df = df[(df[str(header1)].notnull()) & (df[str(header2)].notnull())]
    return df


def findValidResponses(series):
    validResponses = []
    for response in series:
        if response not in validResponses and response != '':
            validResponses.append(response)
    validResponses.sort()
    return validResponses


def generateProbabilityDf(header1, header2):
    df = findSeriesPair(header1, header2, True)
    responses1 = findValidResponses(df[str(header1)])
    responses2 = findValidResponses(df[str(header2)])
    for r1 in responses1:
        pool = df[df[str(header1)] == str(r1)]
        for r2 in responses2:
            matches = df[(df[str(header1)] == str(r1))
                         & (df[str(header2)] == str(r2))]
            p = round(len(matches) / len(pool) * 100)
            print('probability of ' + str(r1) + ' ' + str(header1) + ' with '
                  + str(r2) + ' ' + str(header2) + ' is: ' + str(p) + '%')


generateProbabilityDf('1A Consonant Inventories',
                      '2A Vowel Quality Inventories')
