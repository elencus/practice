import pandas as pd


def findSeries(df, header):
    for series in df:
        if header in str(df[series]):
            return df[series]
    assert False, ('Searched for an invalid series.')


def csvToDf(csv):
    df = pd.read_csv(str(csv))
    return df


def getSeries(df):
    series = []
    for i in df:
        if i in series:
            pass
        else:
            series.append(i)
    return series


def findSeriesPair(df, series, removeNullAnswers):
    frame = {}
    for i in df:
        for j in series:
            if (j in str(df[i])):
                frame[j] = df[i]
    df = pd.DataFrame(frame)
    if removeNullAnswers:
        for i in series:
            df = df[(df[str(i)].notnull())]
    return df


def findValidResponses(series):
    validResponses = []
    for response in series:
        if response not in validResponses and response != '':
            validResponses.append(response)
    validResponses.sort()
    return validResponses


def generatePDf(df, series):
    pDfDict = {}
    header1 = series[0]
    header2 = series[1]
    df = findSeriesPair(df, series, True)
    columns = findValidResponses(df[str(header1)])
    index = findValidResponses(df[str(header2)])
    pDf = pd.DataFrame(columns=columns, index=index)
    for r2 in index:
        pool = df[df[str(header2)] == str(r2)]
        for r1 in columns:
            matches = df[(df[str(header1)] == str(r1))
                         & (df[str(header2)] == str(r2))]
            p = round(len(matches) / len(pool) * 100)
            # if p <= 1:
            #     p = 1
            pDfDict[str(r1)] = p
        pDf.loc[str(r2)] = pDfDict
    print(pDf)
    return(pDf)


# in: pandas dataframe
# out: list of paired columns
def generateColumnPairs(df):
    pairs = []
    for series1 in df:
        for series2 in df:
            if series1 == series2:
                pass
            else:
                pairs.append([series1, series2])
    return pairs


def calculateProbs(csv):
    print('running ok')
    df = pd.read_csv(str(csv))
    seriesPairs = generateColumnPairs(df)
    for pair in seriesPairs:
        generatePDf(df, pair)
