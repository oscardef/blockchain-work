import requests
from web3 import Web3
import json
import pandas as pd

# PROGRAM: before visualizing the data the inputs need to be decoded, this program does that for each transaction hash
# in mergedColumns.csv

bsc = "https://bsc-dataseed.binance.org/"
web3 = Web3(Web3.HTTPProvider(bsc))
print(web3.isConnected())

BSCSCAN_API_KEY = "CP86BMUWHURNS3SXZXN6Z8FT9MAT85MQXA"

# Contract address
CONTRACT_ADDR = Web3.toChecksumAddress("0x064bb6eea2339cad2bdaf895c3d3728e2c6bdac1")
def decodeInputByTxHash(tx_hash):
    # get the transaction
    tx = web3.eth.get_transaction(tx_hash)
    # Get ABI for smart contract NOTE: Use Contract address (not the ["to"] address from the tx)
    # as ["to"] is the proxy contract
    abi_endpoint = f"https://api.bscscan.com/api?module=contract&action=getabi&address={CONTRACT_ADDR}&apikey={BSCSCAN_API_KEY}"
    abi = json.loads(requests.get(abi_endpoint).text)

    # Get the contract from the contract address and abi
    contract = web3.eth.contract(address=CONTRACT_ADDR, abi=abi["result"])
    # get the function and function parameters from the contract and transaction input
    return contract.decode_function_input(tx["input"])


df = pd.read_csv('../reformatCSV/mergedColumns.csv')
# create new dataframe with only Blockno column from df

dfPlot = df.iloc[:, 1]
print(dfPlot)
# for row in df['Txhash'] decodeInputByTxHash(row)
rowNum = 0
print(df.columns[18:])
for row in df['Txhash']:
    func_obj, func_params = decodeInputByTxHash(row)
    print("   #: " + str(rowNum))
    print(func_params)
    if rowNum == 5 or rowNum == 6:
        func_params['_liquidationRatio'] = func_params.pop('_data')
        func_params['_collateralPoolId'] = func_params.pop('_poolId')
    df.loc[rowNum, 'collateralPoolId'] = func_params['_collateralPoolId']
    for column in df.columns[18:]:
        colName = '_' + column
        if colName in func_params.keys():
            print(column)
            print(func_params[colName])
            df.loc[rowNum, column] = func_params[colName]

    rowNum += 1
# set collateralPoolId to type string
df['collateralPoolId'] = df['collateralPoolId'].astype(str)
df['collateralPoolId'] = df['collateralPoolId'].str.split("'", 1).str[1].str.split("\\", 1).str[0]
df.to_csv('decodedData.csv', index=False)
