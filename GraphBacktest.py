import pandas as pd
import requests
import json
import time



def getUnixTime(fromdate):
    timeArray = time.localtime(fromdate)
    unixTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return(unixTime)

def graph(network,Adress,fromdate):
    if network == 1:
        url='https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v3'

    elif network == 2:
        url='https://api.thegraph.com/subgraphs/name/ianlapham/uniswap-arbitrum-one'

    elif network == 3:
        url='https://api.thegraph.com/subgraphs/name/ianlapham/uniswap-optimism-dev'

    unixTime = getUnixTime(fromdate)

    print(f'request ========== Start Time : {unixTime} \n')
    print(f'network = {network} \n')
    print(f'url = {url} \n')
    print(f'Adress = {Adress} \n')

    query = '''
        query
        {
            poolHourDatas(
                where:{
                    pool:"'''+str(Adress)+'''",
                    periodStartUnix_gt:'''+str(fromdate)+'''
                   
                },
                orderBy:periodStartUnix,
                orderDirection:desc,
                first:1000
            )
            {
                periodStartUnix
                liquidity
                high
                low
                pool{
                    volumeUSD
                    collectedFeesUSD
                    totalValueLockedUSD
                    totalValueLockedToken1
                    totalValueLockedToken0
                    token0
                        {decimals
                        }
                    token1
                        {decimals
                        }
                    }
                close
                feeGrowthGlobal0X128
                feeGrowthGlobal1X128

            }
        }
    '''

    

    
    headers = {'Content-Type': 'application/json'}
    data = {'query': query}
    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        # 解析查询结果
        result = json.loads(response.text)
        #print(result)
        
        '''
        pair_hour_datas = result['data']['poolHourDatas']
        for item in pair_hour_datas:
            date = getUnixTime(item['periodStartUnix'])
            volumeUSD = item['pool']['volumeUSD']
            tvlUSD = item['pool']['totalValueLockedUSD']
            collectedFeesUSD = item['pool']['collectedFeesUSD']
            print(f'Date: {date}, Volume USD: {volumeUSD}, tvl USD: {tvlUSD}, col fee USD: {collectedFeesUSD} \n')
        '''

    
        dpd = pd.json_normalize(result['data']['poolHourDatas'])
        dpd = dpd.astype(float)
        print("Rresponse status: 200 (success)\n\n")
    else:
        # Handle error if the API request was not successful
        print("Rresponse Error: Failed to fetch data from the API\n\n")
    return dpd

