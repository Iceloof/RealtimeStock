import requests
import time
import json
import random
import time
import pytz, datetime

user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:64.0) Gecko/20100101 Firefox/64.0'
headers = {'User-Agent': user_agent}

def sinaQuote(market, stock_code):
    try:
        current = datetime.datetime.now(tz=pytz.timezone('Asia/Hong_Kong')).strftime("%Y-%m-%d %H:%M:%S")
        if market == 'hk' and datetime.datetime.now(tz=pytz.timezone('Asia/Hong_Kong')).strftime("%H:%M:%S") > "16:00:00":
            current = datetime.datetime.now(tz=pytz.timezone('Asia/Hong_Kong')).strftime("%Y-%m-%d 16:00:00")
        elif (market == 'hk' or market == 'sh' or market == 'sz') and datetime.datetime.now(tz=pytz.timezone('Asia/Hong_Kong')).strftime("%H:%M:%S") < "09:30:00":
            day = 1
            while (datetime.datetime.now(tz=pytz.timezone('Asia/Hong_Kong')) - datetime.timedelta(days=day)).strftime("%w")*1 == '6' or (datetime.datetime.now(tz=pytz.timezone('Asia/Hong_Kong')) - datetime.timedelta(days=day)).strftime("%w") == '0':
                day += 1
            current = (datetime.datetime.now(tz=pytz.timezone('Asia/Hong_Kong')) - datetime.timedelta(days=day)).strftime("%Y-%m-%d 16:00:00")
        elif (market == 'sh' or market == 'sz') and datetime.datetime.now(tz=pytz.timezone('Asia/Hong_Kong')).strftime("%H:%M:%S") > "15:00:00":
            current = datetime.datetime.now(tz=pytz.timezone('Asia/Hong_Kong')).strftime("%Y-%m-%d 15:00:00")
        elif market == 'us' and datetime.datetime.now(tz=pytz.timezone('America/New_York')).strftime("%H:%M:%S") > "16:00:00":
            current = datetime.datetime.now(tz=pytz.timezone('America/New_York')).strftime("%Y-%m-%d 16:00:00")
        elif market == 'us' and datetime.datetime.now(tz=pytz.timezone('America/New_York')).strftime("%H:%M:%S") < "09:30:00":
            day = 1
            while (datetime.datetime.now(tz=pytz.timezone('America/New_York')) - datetime.timedelta(days=day)).strftime("%w")*1 == '6' or (datetime.datetime.now(tz=pytz.timezone('Asia/Hong_Kong')) - datetime.timedelta(days=day)).strftime("%w") == '0':
                day += 1
            current = (datetime.datetime.now(tz=pytz.timezone('America/New_York')) - datetime.timedelta(days=1)).strftime("%Y-%m-%d 16:00:00")
        url = "http://hq.sinajs.cn/?list=" + market + stock_code
        r = requests.get(url)
        result = r.text.split(';')[:-1]
        results = []
        for item in result:
            data = item.split('=')[1].split(',')
            if market == 'hk':
                results.append({'code': item.split('=')[0][13:], 'name': data[1], 'en_name': data[0][1:], 'price': float(data[6]), 'time': current})
            else:
                results.append({'code': item.split('=')[0][13:], 'name': data[0][1:], 'price': float(data[3]), 'time': current})
        if len(stock_code.split(',')) == 1:
            results = results[0]
        return results
    except:
        return {'code': stock_code, 'name': '', 'price': -9999999, 'time': ''}

def futuQuote(market, stock_code):
    try:
        current = datetime.datetime.now(tz=pytz.timezone('Asia/Hong_Kong')).strftime("%Y-%m-%d %H:%M:%S")
        if market == 'hk' and datetime.datetime.now(tz=pytz.timezone('Asia/Hong_Kong')).strftime("%H:%M:%S") > "16:00:00":
            current = datetime.datetime.now(tz=pytz.timezone('Asia/Hong_Kong')).strftime("%Y-%m-%d 16:00:00")
        elif (market == 'hk' or market == 'sh' or market == 'sz') and datetime.datetime.now(tz=pytz.timezone('Asia/Hong_Kong')).strftime("%H:%M:%S") < "09:30:00":
            day = 1
            while (datetime.datetime.now(tz=pytz.timezone('Asia/Hong_Kong')) - datetime.timedelta(days=day)).strftime("%w")*1 == '6' or (datetime.datetime.now(tz=pytz.timezone('Asia/Hong_Kong')) - datetime.timedelta(days=day)).strftime("%w") == '0':
                day += 1
            current = (datetime.datetime.now(tz=pytz.timezone('Asia/Hong_Kong')) - datetime.timedelta(days=day)).strftime("%Y-%m-%d 16:00:00")
        elif (market == 'sh' or market == 'sz') and datetime.datetime.now(tz=pytz.timezone('Asia/Hong_Kong')).strftime("%H:%M:%S") > "15:00:00":
            current = datetime.datetime.now(tz=pytz.timezone('Asia/Hong_Kong')).strftime("%Y-%m-%d 15:00:00")
        elif market == 'us' and datetime.datetime.now(tz=pytz.timezone('America/New_York')).strftime("%H:%M:%S") > "16:00:00":
            current = datetime.datetime.now(tz=pytz.timezone('America/New_York')).strftime("%Y-%m-%d 16:00:00")
        elif market == 'us' and datetime.datetime.now(tz=pytz.timezone('America/New_York')).strftime("%H:%M:%S") < "09:30:00":
            day = 1
            while (datetime.datetime.now(tz=pytz.timezone('America/New_York')) - datetime.timedelta(days=day)).strftime("%w")*1 == '6' or (datetime.datetime.now(tz=pytz.timezone('Asia/Hong_Kong')) - datetime.timedelta(days=day)).strftime("%w") == '0':
                day += 1
            current = (datetime.datetime.now(tz=pytz.timezone('America/New_York')) - datetime.timedelta(days=1)).strftime("%Y-%m-%d 16:00:00")
        date = str(time.time()).split(".")
        url = "https://www.futunn.com/trade/search?k=" + stock_code
        r = requests.get(url, headers=headers)
        result = r.json()
        security_id = result['data'][0]['security_id']
        name = result['data'][0]['sc_name']
        en_name = result['data'][0]['en_name']
        url = "https://www.futunn.com/trade/quote-basic-v3?security_id=" + str(security_id) + "&_=" + date[0] + date[1]
        r = requests.get(url, headers=headers)
        data = r.json()
        return {'code': stock_code, 'name': name, 'en_name': en_name, 'price': float(data['data']['quote']['price']), 'time': current}
    except:
        return {'code': stock_code, 'name': '', 'en_name':'', 'price': -9999999, 'time': ''}

def tigerQuote(market, stock_code):
    try:
        if market == 'hk':
            url = "https://www.laohu8.com/proxy/stock/hkstock/stock_info/detail/" + stock_code
        elif market == 'sh' or market == 'sz':
            url = "https://www.laohu8.com/proxy/stock/astock/stock_info/detail/" + stock_code
        else:
            url = "https://www.laohu8.com/proxy/stock/stock_info/detail/" + stock_code
        r = requests.get(url, headers=headers)
        result = r.json()
        if result['items'][0]['market'] == 'US':
            current = datetime.datetime.fromtimestamp(result['items'][0]['timestamp']/1000, pytz.timezone('America/New_York')).strftime("%Y-%m-%d %H:%M:%S")
        else:
            current = datetime.datetime.fromtimestamp(result['items'][0]['timestamp']/1000, pytz.timezone('Asia/Hong_Kong')).strftime("%Y-%m-%d %H:%M:%S")
        return {'code': stock_code, 'name': result['items'][0]['nameCN'], 'price': float(result['items'][0]['latestPrice']), 'time': current}
    except:
        return {'code': stock_code, 'name': '', 'price': -9999999, 'time': ''}

def xueqiuQuote(market, stock_code):
    try:
        session = requests.Session()
        session.get('https://xueqiu.com',headers=headers)
        if market == 'sh' or market == 'sz':
            url = "https://stock.xueqiu.com/v5/stock/quote.json?symbol=" + market.upper() + stock_code + "&extend=detail"
        else:
            url = "https://stock.xueqiu.com/v5/stock/quote.json?symbol=" + stock_code + "&extend=detail"
        r = session.get(url, headers=headers)
        result = r.json()
        return {'code': stock_code, 'name': result['data']['quote']['name'], 'price': float(result['data']['quote']['current']), 'time': datetime.datetime.fromtimestamp(int(result['data']['quote']['timestamp']/1000), pytz.timezone(result['data']['market']['time_zone'])).strftime("%Y-%m-%d %H:%M:%S")}
    except:
        return {'code': stock_code, 'name': '', 'price': -9999999, 'time': ''}

def tencentQuote(market, stock_code):
    try:
        current = datetime.datetime.now(tz=pytz.timezone('Asia/Hong_Kong')).strftime("%Y-%m-%d %H:%M:%S")
        if market == 'hk' and datetime.datetime.now(tz=pytz.timezone('Asia/Hong_Kong')).strftime("%H:%M:%S") > "16:00:00":
            current = datetime.datetime.now(tz=pytz.timezone('Asia/Hong_Kong')).strftime("%Y-%m-%d 16:00:00")
        elif (market == 'hk' or market == 'sh' or market == 'sz') and datetime.datetime.now(tz=pytz.timezone('Asia/Hong_Kong')).strftime("%H:%M:%S") < "09:30:00":
            day = 1
            while (datetime.datetime.now(tz=pytz.timezone('Asia/Hong_Kong')) - datetime.timedelta(days=day)).strftime("%w")*1 == '6' or (datetime.datetime.now(tz=pytz.timezone('Asia/Hong_Kong')) - datetime.timedelta(days=day)).strftime("%w") == '0':
                day += 1
            current = (datetime.datetime.now(tz=pytz.timezone('Asia/Hong_Kong')) - datetime.timedelta(days=day)).strftime("%Y-%m-%d 16:00:00")
        elif (market == 'sh' or market == 'sz') and datetime.datetime.now(tz=pytz.timezone('Asia/Hong_Kong')).strftime("%H:%M:%S") > "15:00:00":
            current = datetime.datetime.now(tz=pytz.timezone('Asia/Hong_Kong')).strftime("%Y-%m-%d 15:00:00")
        elif market == 'us' and datetime.datetime.now(tz=pytz.timezone('America/New_York')).strftime("%H:%M:%S") > "16:00:00":
            current = datetime.datetime.now(tz=pytz.timezone('America/New_York')).strftime("%Y-%m-%d 16:00:00")
        elif market == 'us' and datetime.datetime.now(tz=pytz.timezone('America/New_York')).strftime("%H:%M:%S") < "09:30:00":
            day = 1
            while (datetime.datetime.now(tz=pytz.timezone('America/New_York')) - datetime.timedelta(days=day)).strftime("%w")*1 == '6' or (datetime.datetime.now(tz=pytz.timezone('Asia/Hong_Kong')) - datetime.timedelta(days=day)).strftime("%w") == '0':
                day += 1
            current = (datetime.datetime.now(tz=pytz.timezone('America/New_York')) - datetime.timedelta(days=1)).strftime("%Y-%m-%d 16:00:00")
        date = str(time.time()).split(".")
        url = "http://qt.gtimg.cn/?q=s_" + market + stock_code +"&_=" + date[0] + date[1]
        r = requests.get(url, headers=headers)
        result = r.text.split(';')[:-1]
        results = []
        for item in result:
            data = item.split('=')[1].split('~')
            results.append({'code': stock_code, 'name': data[1], 'price': float(data[3]), 'time': current})
        if len(stock_code.split(',')) == 1:
            results = results[0]
        return results
    except:
        return {'code': stock_code, 'name': '', 'en_name':'', 'price': -9999999, 'time': ''}

def getQuote(market, stock_code):
    result = {'code': stock_code, 'name': '', 'price': -9999999, 'time': ''}
    if market == 'us':
        value = random.randint(3,5)
    elif market == 'hk':
        value = random.randint(4,5)
    else:
        value = random.randint(3,5)
    if value == 1:
        r = sinaQuote(market, stock_code)
    elif value == 2:
        r = futuQuote(market, stock_code)
    elif value == 3:
        r = tencentQuote(market, stock_code)
    elif value == 4:
        r = xueqiuQuote(market, stock_code)
    elif value == 5:
        r = tigerQuote(market, stock_code)
    result['code'] = r['code']
    result['name'] = r['name']
    result['price'] = r['price']
    result['time'] = r['time']
    return result
