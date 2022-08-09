import pandas as pd

df = pd.read_csv('data_new.csv')

df1 = df.iloc[:, :29]
df2 = df.iloc[:, 30:]

for column in df2.columns:
    df2.rename(columns={column: column.split(".", 1)[0]}, inplace=True)

for column in df2.columns:
    if column == "collateralPoolId":
        continue
    rowNum = 0
    for row in df2[column]:
        if type(row) is str:
            df1.loc[rowNum, column] = row
        rowNum += 1

df1.to_csv('mergedColumns.csv', index=False)
