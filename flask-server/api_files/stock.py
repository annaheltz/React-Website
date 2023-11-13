import requests
from datetime import datetime, date, time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import io
import base64
from matplotlib.ticker import MaxNLocator

ticker = "AAPL"
api_key1 = "x"
api_key2 = "x"
api_key3 = "x"
api_key4 = 'x'
interval = '1min'


def get_stock_price(ticker_symbol):
    url = f"https://api.twelvedata.com/price?symbol={ticker_symbol}&apikey={api_key1}"
    response = requests.get(url)
    if response.status_code == 200:
        # Request was successful
        data = response.json()
        if('code' in data):
            return "Failed"
        price = data['price'][:-3]
        return price
    else:
        return "Failed"


def get_stock_quote(ticker_symbol):
    url = f"https://api.twelvedata.com/quote?symbol={ticker_symbol}&apikey={api_key2}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if('code' in data):
            return "Failed"
        info = data['name'] + '<br> Open: ' + data['open'] + '<br> High: ' + data['high'] + '<br> Low: ' + data['low'] + '<br> Close: ' + data['close'] 
        return info        
    else:
        return "Failed"

# supports 1min, 5min, 15min, 30min, 45min, 1h, 2h, 4h, 1day, 1week, 1month
def get_stock_timeseries(ticker_symbol, interval):
    if(interval == '1min'):
        url = f"https://api.twelvedata.com/time_series?symbol={ticker_symbol}&interval={interval}&apikey={api_key3}"
    else:
        url = f"https://api.twelvedata.com/time_series?symbol={ticker_symbol}&interval={interval}&apikey={api_key4}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if('code' in data):
            return "Failed"
        return data
    else:
        return "Failed"

def createGraph(ticker_symbol, interval):
    timeseries = get_stock_timeseries(ticker_symbol, interval)
    date_format = '%Y-%m-%d %H:%M:%S'
    if(timeseries == "Failed"):
            return "Failed"
    values = timeseries['values']
    dates = []
    open = []
    high = []
    low = []
    close = []
    for item in values:        
        get_date = item['datetime']
        if interval == "1day":
            get_date = get_date + ' 00:00:00'
            
        dates.append(datetime.strptime(get_date, date_format))
        open.append(float(item['open']))
        high.append(float(item['high']))
        low.append(float(item['low']))
        close.append(float(item['close']))
    # Create a line graph
    fig, ax = plt.subplots()
    ax.plot(dates, open, label='Stock Price')

    # Add labels and a legend
    
    ax.set_ylabel('open')
    ax.xaxis.set_major_locator(MaxNLocator(8))
    if interval == "1min":
        ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%I:%M'))
        ax.set_title(ticker_symbol + " in recent minutes")
        ax.set_xlabel('minutes')
    else:
        ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%m-%d'))
        ax.set_title(ticker_symbol + " in recent days")
        ax.set_xlabel('dates')
    ax.legend()

    # Save the figure to a BytesIO buffer and convert to base64
    buffer = io.BytesIO()
    fig.savefig(buffer, format='png')
    buffer.seek(0)
    image_data = base64.b64encode(buffer.read()).decode()
    buffer.close()
    return image_data
