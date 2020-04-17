import pandas as pd


# IN: csv file
# OUT: pandas dataframe
def csvToDf(csv):
    df = pd.read_csv(str(csv))
    return df


# IN: pandas dataframe, list of series we want to find, boolean
# if we want to remove empty cells.
# OUT: dataframe with only the series we requested
def findSeries(df, series, removeNullAnswers):
    frame = {}
    for i in series:
        frame[i] = df[i]
    df = pd.DataFrame(frame)
    if removeNullAnswers:
        for i in series:
            df = df[(df[str(i)].notnull())]
    return df


# IN: list of series
# OUT: list of all possible values in that series
def findValidResponses(series):
    validResponses = []
    for response in series:
        if response not in validResponses and response != '':
            validResponses.append(response)
    validResponses.sort()
    return validResponses


# IN: pandas dataframe, list of 2 series as strings
# OUT: a dataframe of the probability that a given response
# in one series matches with a given response in another series
def generatePDf(df, series):
    if len(series) > 2:
        raise ValueError("Cannot compare more than two columns at a time.")
    pDfDict = {}
    headers = []
    for s in series:
        headers.append(s)
    pDfDict = {}
    df = findSeries(df, series, True)
    columns = findValidResponses(df[str(headers[0])])
    index = findValidResponses(df[str(headers[1])])
    pDf = pd.DataFrame(columns=columns, index=index)
    for r2 in index:
        pool = df[df[str(headers[1])] == str(r2)]
        for r1 in columns:
            matches = df[(df[str(headers[0])] == str(r1))
                         & (df[str(headers[1])] == str(r2))]
            p = round(len(matches) / len(pool) * 100)
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
