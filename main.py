from pycoingecko import CoinGeckoAPI
import pandas as pd

cg = CoinGeckoAPI()
lst = cg.get_coin_market_chart_by_id(id = 'bitcoin', vs_currency = 'USD', days = 4600)
lst = lst['prices']

def Extract(lst):
    return [item[0] for item in lst]
unix = Extract(lst)
unix

def Extract(lst):
    return [item[1] for item in lst]
priceLst = Extract(lst)
priceLst

import math
price = []
for i in priceLst:
    p = (math.floor(i))
    price.append(p)
price

import datetime

time = []
for i in unix:
    timestamp_with_ms = i
    dt = datetime.datetime.fromtimestamp(timestamp_with_ms / 1000)
    formatted_time = dt.strftime('%Y-%m-%d %H')[:-3]
#     formatted_time = formatted_time.replace("-", '')
    time.append(formatted_time)
df = pd.DataFrame(price)

df['time'] = time
df.columns = ['Price','Time']
df = df.reset_index(drop=True)

date = input("Enter date in the form YYYY-MM-DD : ")
invAmt = int(input("Enter Amount You Would Have Invested  : "))

if date in df.values:
    idx = (df[df['Time'] == date].index.values)
    priceAtDate = int(df.loc[idx]['Price'])
else:
    print("Incorrect Date")

currentPrice = cg.get_price(ids = 'bitcoin', vs_currencies = 'USD')
currentPrice = currentPrice['bitcoin']['usd']
percentageGrowth = (currentPrice/priceAtDate) *100
nbtc = invAmt/priceAtDate
currValue = nbtc * currentPrice

growth = ''
priceAtDate = int(df.loc[idx]['Price'])
if priceAtDate > currentPrice:
    growth = 'depreciation'

elif priceAtDate < currentPrice :
    growth = 'appreciation'
    
percentageGrowth =''
if growth == 'appreciation':
    perGrowth = (currentPrice/priceAtDate) *100
    percentageGrowth = perGrowth
elif growth == 'depreciation':
    perGrowth = 100 -  ((currentPrice/priceAtDate) *100)
    percentageGrowth = perGrowth


result = (f"Your investment of ${invAmt} on {date} would have been $ {round(currValue, 2)} today with a {growth} of {round(percentageGrowth, 2)} %")
res2 = f"Value of 1 Btc on {date} was {priceAtDate} "
res3 = f"Value of 1 Btc today is {currentPrice} "

print(res2)
print(res3)

print(result)
