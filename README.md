# RealtimeStock

[![Build Status](https://travis-ci.com/Iceloof/RealtimeStock.svg)](https://travis-ci.com/Iceloof/RealtimeStock)
[![Coverage Status](https://coveralls.io/repos/github/Iceloof/RealtimeStock/badge.svg)](https://coveralls.io/github/Iceloof/RealtimeStock)
[![PyPI](https://img.shields.io/pypi/v/RealtimeStock)](https://pypi.org/project/RealtimeStock/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/RealtimeStock)](https://pypistats.org/packages/realtimestock)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/RealtimeStock)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/RealtimeStock)
![GitHub contributors](https://img.shields.io/github/contributors/Iceloof/RealtimeStock)
![GitHub issues](https://img.shields.io/github/issues-raw/Iceloof/RealtimeStock)
![GitHub Action](https://github.com/Iceloof/RealtimeStock/workflows/GitHub%20Action/badge.svg)
![GitHub](https://img.shields.io/github/license/Iceloof/RealtimeStock)

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

- Get realtime quote (ShanghaiExchange)
```
print(sinaQuote("sh","600320"))
print(futuQuote("sh","600320"))
print(tigerQuote("sh","600320"))
print(tencentQuote("sh","600320"))
print(getQuote("sh","600320"))
```

- Get realtime quote (Shenzhen Exchange)
```
print(sinaQuote("sz","002122"))
print(futuQuote("sz","002122"))
print(tigerQuote("sz","002122"))
print(tencentQuote("sz","002122"))
print(getQuote("sz","002122"))
```

- Get realtime quote (NASDAQ/NYSE/AMEX) * `sinaQuote` is not supported
```
print(futuQuote("us","VRSK"))
print(tigerQuote("us","VRSK"))
print(tencentQuote("us","VRSK"))
print(getQuote("us","VRSK"))
```
