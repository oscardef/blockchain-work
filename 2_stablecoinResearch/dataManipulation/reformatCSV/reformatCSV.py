import pandas as pd
import re
# PROGRAM: read data.csv and add a new column for each input in the 'Input' column and place the corresponding
# input to that column and save the final result as 'data_inputs.csv'
# after running this column names in 'data_inputs.csv' are renamed as seen in 'data_new.csv'

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
df.to_csv('data_inputs.csv', index=False)
