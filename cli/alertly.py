


import requests
import logging
import os
from subprocess import check_output, check_call, CalledProcessError, STDOUT
import shutil
import click
import urllib.request  
import hashlib
import json
import re
from alert import Alert
from kucoin.client import Market
import threading
import sys 
from threading import Timer
from pprint import pprint


class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.daemon   = True
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)
        

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False


CLIENT = Market(url='https://api.kucoin.com')

cached_price = []
def do_out(cmd):
    print(cmd)
    try:
        output = check_output(re.split(r'\s+', cmd), stderr=STDOUT).decode()
    except CalledProcessError as e:
        output = e.output.decode()
    print(output)

def cache_price(price):
    if len(cached_price) > 9:
        cached_price.pop(0)
    else:
        cached_price.append(price)

    return cached_price

def get_ticker(ticker):
    # get symbol kline    
    price = CLIENT.get_ticker(ticker)['price']
    print(ticker,':',price)
    cache_price(price)

def get_tickers():
    tickers = CLIENT.get_all_tickers()['ticker']
    f = open("tickers.txt", "a")
    for ticker in tickers:
        f.write(ticker['symbol']+'\n')
    f.close()

def find_pairs(ticker):
    pairs = []
    get_tickers()
    f = open("tickers.txt", "r").read().split('\n')
    for x in f:
        if ticker in x.split('-')[0].lower():
            pairs.append(x)
    pprint(pairs)

    return pairs



@click.command()
@click.option('-t', '--ticker', help='get specific ticker ie BTC-USDT',required=False)
@click.option('-p', '--pair', help='find all pair associated with ticker',required=False)
@click.option('--gettickers', is_flag=True, help='get all tickers outputs everything in tickers.txt')
def cli(ticker, gettickers,pair):
    if ticker:
        alert = RepeatedTimer(2, get_ticker, ticker)
    if gettickers:
        get_tickers()
    if pair:
        find_pairs(pair)
    
    

if __name__ == '__main__':
    cli()
    # alert = RepeatedTimer(10, get_ticker, 'BTC-USDT')
    
    