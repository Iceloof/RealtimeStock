# RealtimeStock

<!--- 
[![Build Status](https://travis-ci.com/Iceloof/RealtimeStock.svg)](https://travis-ci.com/Iceloof/RealtimeStock)
[![Coverage Status](https://coveralls.io/repos/github/Iceloof/RealtimeStock/badge.svg)](https://coveralls.io/github/Iceloof/RealtimeStock)
![GitHub Action](https://github.com/Iceloof/RealtimeStock/workflows/GitHub%20Action/badge.svg)
--->
[![PyPI](https://img.shields.io/pypi/v/RealtimeStock)](https://pypi.org/project/RealtimeStock/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/RealtimeStock)](https://pypistats.org/packages/realtimestock)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/RealtimeStock)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/RealtimeStock)
![GitHub contributors](https://img.shields.io/github/contributors/Iceloof/RealtimeStock)
![GitHub issues](https://img.shields.io/github/issues-raw/Iceloof/RealtimeStock)
![GitHub](https://img.shields.io/github/license/Iceloof/RealtimeStock)

This package is supported realtime stock quote from Shanghai Exchange, Shenzhen Exchange, HongKong Exchange, and US Market(NASDAQ, NYSE, AMEX).

- The method `futuQuote`, `futuQuoteById`, `tigerQuote` and `tencentQuote` support all the markets, `sinaQuote` is not support US Market. 
- The method `getQuote` will random choose one of the method to get the realtime quote, this will avoid being blocked by one of the sources when doing heavy requests.

## Install
```
pip install RealtimeStock
```
or
```
pip install --upgrade RealtimeStock
```

## Usage
- Initializing
```
from RealtimeStock import sinaQuote, futuQuote, futuQuoteById, tigerQuote, tencentQuote, getQuote
```

- Get realtime quote (HKEX)
```
print(sinaQuote("hk","07200"))
print(futuQuote("hk","07200"))
print(tigerQuote("hk","07200"))
print(tencentQuote("hk","07200"))
print(getQuote("hk","07200"))
```
Sample output
```
{'code': '07200', 'name': 'ＦＬ二南方恒指', 'en_name': '"FL2 CSOP HSI', 'price': 8.74, 'time': '2020-11-16 16:00:00'}
{'code': '07200', 'name': '南方两倍看多恒指', 'en_name': 'CSOP HANG SENG INDEX DAILY', 'price': 8.74, 'time': '2020-11-16 16:00:00'}
{'code': '07200', 'name': 'FL二南方恒指', 'price': 8.74, 'time': '2020-11-16 16:08:36'}
{'code': '07200', 'name': 'FL二南方恒指', 'price': 8.74, 'time': '2020-11-16 16:00:00'}
{'code': '07200', 'name': 'FL二南方恒指', 'price': 8.74, 'time': '2020-11-16 16:08:36'}
```

- Get realtime quote (ShanghaiExchange)
```
print(sinaQuote("sh","600320"))
print(futuQuote("sh","600320"))
print(tigerQuote("sh","600320"))
print(tencentQuote("sh","600320"))
print(getQuote("sh","600320"))
```
Sample output
```
{'code': '600320', 'name': '"振华重工', 'price': 3.07, 'time': '2020-11-16 15:00:00'}
{'code': '600320', 'name': '振华重工', 'en_name': 'Shanghai Zhenhua Heavy Industries', 'price': 3.07, 'time': '2020-11-16 15:00:00'}
{'code': '600320', 'name': '振华重工', 'price': 3.07, 'time': '2020-11-16 15:03:57'}
{'code': '600320', 'name': '振华重工', 'price': 3.07, 'time': '2020-11-16 15:00:00'}
{'code': '600320', 'name': '振华重工', 'price': 3.07, 'time': '2020-11-16 15:03:57'}
```

- Get realtime quote (Shenzhen Exchange)
```
print(sinaQuote("sz","002122"))
print(futuQuote("sz","002122"))
print(tigerQuote("sz","002122"))
print(tencentQuote("sz","002122"))
print(getQuote("sz","002122"))
```
Sample output
```
{'code': '002122', 'name': '"*ST天马', 'price': 2.17, 'time': '2020-11-16 15:00:00'}
{'code': '002122', 'name': '*ST天马', 'en_name': 'Tianma Bearing Group', 'price': 2.17, 'time': '2020-11-16 15:00:00'}
{'code': '002122', 'name': '*ST天马', 'price': 2.17, 'time': '2020-11-16 15:03:03'}
{'code': '002122', 'name': '*ST天马', 'price': 2.17, 'time': '2020-11-16 15:00:00'}
{'code': '002122', 'name': '"*ST天马', 'price': 2.17, 'time': '2020-11-16 15:00:00'}
```

- Get realtime quote (NASDAQ/NYSE/AMEX) 
```
print(futuQuote("us","VRSK"))
print(tigerQuote("us","VRSK"))
print(tencentQuote("us","VRSK"))
print(getQuote("us","VRSK"))
```
Sample output
```
{'code': 'VRSK', 'name': 'Verisk Analytics', 'en_name': 'Verisk Analytics Inc', 'price': 203.7, 'time': '2020-11-15 16:00:00'}
{'code': 'VRSK', 'name': 'Verisk Analytics', 'price': 203.7, 'time': '2020-11-13 16:00:00'}
{'code': 'VRSK', 'name': 'Verisk Analytics Inc', 'price': 203.7, 'time': '2020-11-15 16:00:00'}
{'code': 'VRSK', 'name': 'Verisk Analytics', 'price': 203.7, 'time': '2020-11-15 16:00:00'}
```
