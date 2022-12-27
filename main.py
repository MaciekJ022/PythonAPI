import time
from datetime import datetime
import requests
from threading import Thread


def showTime():
    while True:
        currentDate = datetime.now().strftime('%d/%b/%Y %H:%M:%S')
        print(f'Current date: {currentDate}')
        time.sleep(1)

def getBitcoinUSD():
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = response.json()

    while True:
        priceUSD = data['bpi']['USD']['rate']
        print(f'Bitcoin price in USD: {priceUSD}')
        time.sleep(10)

T1 =  Thread(target=showTime)
T1.start()

T2 =  Thread(target=getBitcoinUSD())
T2.start()

while True:
    T1.join()
    T2.join()