修正 uniswap-v3-backtest-python 無法執行的問題

1. requests 改用 post

2. 目前限定使用Ethereum (network = 1)
   
   因為arbitrum 的 subgraphs 缺少以下2個欄位故暫無法執行
     
   feeGrowthGlobal0X128
   
   feeGrowthGlobal1X128

==============================   

原程式碼進行下列安裝後即可執行

pip install "gql[all]"
