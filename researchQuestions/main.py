import requests
from web3 import Web3
import json
import pandas as pd
import numpy as np

bsc = "https://bsc-dataseed.binance.org/"
web3 = Web3(Web3.HTTPProvider(bsc))
print(web3.isConnected())

BSCSCAN_API_KEY = "CP86BMUWHURNS3SXZXN6Z8FT9MAT85MQXA"

# Contract address
CONTRACT_ADDR = Web3.toChecksumAddress("0xe35e008CCb407448EF37eF7C0148097553C00aA0")


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


# create new dataframe with only with an extra column for row numbers
df = pd.read_csv('collect.csv', header=0, index_col=False)

# for row in df['Txhash'] decodeInputByTxHash(row)
rowNum = 0
print(df.columns)
df['collateralPool'] = np.nan
for row in df['Txhash']:
    if rowNum == 0:
        rowNum += 1
        continue
    func_obj, func_params = decodeInputByTxHash(row)
    print(func_params)
    print(func_obj)
    df.loc[rowNum, 'collateralPool'] = func_params['_collateralPool']
    rowNum += 1
# set collateralPool to type string
df['collateralPool'] = df['collateralPool'].astype(str)
df['collateralPool'] = df['collateralPool'].str.split("'", 1).str[1].str.split("\\", 1).str[0]
print(df['collateralPool'])
df.to_csv('decodedCollect.csv', index=False)
