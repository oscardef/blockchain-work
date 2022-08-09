import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('decodedData.csv')

for column in df.columns[19:]:
    if type(df[column][0]) is str:
        if df[column][0][1] == 'x':
            continue
    dfNew = pd.DataFrame().assign(DateTime=df['DateTime'], Data=df[column])
    dfNew = dfNew.dropna()
    dfNew['Data'] = dfNew['Data'].astype(float)
    plt.plot(dfNew['DateTime'], dfNew['Data'], drawstyle='steps')
    plt.title(column)
    plt.rcParams["figure.figsize"] = (10, 6)
    plt.xticks(rotation=25)
    plt.savefig('plots/' + column + '.png', bbox_inches='tight')
    plt.show()
