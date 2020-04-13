import pandas as pd

walsData = pd.read_csv('language.csv')


def findSeries(header):
    for series in walsData:
        if header in str(walsData[series]):
            return walsData[series]
    assert False, ('Searched for an invalheader series.')


findSeries('130B')
