import pandas as pd
import re

df = pd.read_csv('data.csv', header=0)
rowNum = 0
for row in df['Input (Default)']:
    inputs = row.split('\n')
    method = df['Method'][rowNum]
    cnt = 0
    for i in inputs:
        cnt += 1
        num = re.search(r"\[(\w+)", i).group(1)
        inputNum = str(" #" + num)
        index = inputs.index(i)
        inputs[index] = i.replace(i[0:6], '')
        colName = method+inputNum
        if colName not in df.columns:
            df[colName] = ""
        df.loc[rowNum, colName] = inputs[index]
    rowNum += 1
df.to_csv('data_new.csv', index=False)
