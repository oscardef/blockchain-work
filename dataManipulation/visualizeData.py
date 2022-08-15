import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv('decodedData.csv')

d = dict(tuple(df.groupby('collateralPoolId')))

for key in d.keys():
    for column in d[key].columns[19:]:
        # don't create a plot for columns with addresses
        if type(df[column][0]) is str:
            if df[column][0][1] == 'x':
                continue
        dfNew = pd.DataFrame().assign(DateTime=d[key]['DateTime'], Data=d[key][column])
        dfNew = dfNew.dropna()
        dfNew['Data'] = dfNew['Data'].astype(float)
        if dfNew['DateTime'].size == 1:
            plt.plot(dfNew['DateTime'], dfNew['Data'], marker="o", markersize=10)
        else:
            plt.plot(dfNew['DateTime'], dfNew['Data'], drawstyle='steps-post')
        plt.title(key + '\n' + column)
        plt.rcParams["figure.figsize"] = (10, 6)
        plt.xticks(rotation=25)
        path = './plots/' + key
        # Check whether the specified path exists or not
        isExist = os.path.exists(path)
        #print(isExist)
        if not isExist:
            # Create a new directory because it does not exist
            os.makedirs(path)
            #print("The new directory is created!")
        plt.savefig('plots/' + key + '/' + column + '_' + key + '.png', bbox_inches='tight')
        plt.show()


