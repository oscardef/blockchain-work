from bscscan import BscScan
import asyncio
import pandas as pd


async def find_contract(contract_address):
    async with BscScan("CP86BMUWHURNS3SXZXN6Z8FT9MAT85MQXA") as client:
        contract = await client.get_contract_source_code(contract_address)
        contract_dict = contract[0]
        print(contract_dict.get('ContractName') + ": " + contract_address)

df = pd.read_csv('alldata.csv', header=0)
rowNum = 0
for row in df['ContractAddress']:
    if type(row) is str:
        asyncio.run(find_contract(row))
