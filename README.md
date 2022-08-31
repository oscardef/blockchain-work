# blockchain-work

Internship work I did as a Blockchain Engineering intern in the summer of 2022. The work involved 3 main phases.


## 1. (2 weeks)

I began by following the CryptoZombies course on cryptozombies.io/en/course. This course helped me understand all the fundamentals of Solidity, tokenisation, ERC20. & ERC721 tokens, oracles, ethereum, web3, some javascript front-end, and many other interesting blockchain features.

The course gave me exactly what I required to be able to make my own tokens as well as a wallet that can store and make transactions with these tokens.


## 2. (2 weeks)

After completion of the course I was tasked with creating my own ERC20 and ERC721 tokens, along with a Wallet that is able to store and transact ERC20 tokens. This work can be seen in '1_tokenCreation'.


## 3. (1 month)

The last and longest part of my internship involved research pertaining stablecoins and stablecoin data. This began with me looking into Alpaca and MakerDAO seen in '2_stablecoinResearch'. Initially this was normal research; finding out what the two organizations were, how the functioned, and the some similarities and diffrences. From there I was tasked with focusin in on alpaca and working with more onchain data. All my work regarding the stablecoin research and data manipulation is briefly documented in the appropriate files and scripts, but I will give a brief overview of the main components.


#### ReformatCSV:

  In the reformatCSV directory my main task was to simply get familiarized with dataManipulation. I wrote the reformatCSV.py script to simply split one column containing a lot of input data, into individual columns for each piece of data, and then wrote the mergeColumns.py script to merge the data in a more meaningful and useable way. The final useful file from this directory is mergedColumns.csv


#### VisualizeData:

  In the visualizeData directory shows my task involving visualizing some of the data I was working with previously. I first wrote the preVisualization.py script to clean the data a bit more and decode the inputs in a meaningful way for the data visualization. I then wrote visualizeData.py to to greate the actual plots shows in the subdirectories of the 'plots' directory.


#### SearchBscScan:

  The searchBscScan directory contains one of the most useful scripts I wrote during this period. Large parts of my research work involved taking addresses from a csv file, going to bscScan, and checking if that address corresponded to the contract I was looking for. This process was repetivitve, and tedious; perfect for a program to do for me. So my searchBscScan.py script connects to the bscScan API and takes all the contract addresses related to AlpacaUSD that ive downloaded into a csv file called alpacaData.csv and it simply prints outs all contracts and contract addresses that appear in the contract in a neat fashion. This helps me quikcly find the contracts I'm looking for and I can start putting time into the research involving them more so than actually finding them.
  
  
#### AlpacaResearch:

  The AlpacaResearch directory contains some more in-depth alpaca research that I did pertaining the Alpaca contracts. It consits of more deeply documented functions, some diagrams depicting function and collateral flow, and answers to a couple research questions I was tasked with looking into.
  
  
  
Overall I learnt a lot during this internship and I will take many skills with me into my future work.
