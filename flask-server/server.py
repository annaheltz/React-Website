from flask import Flask, render_template
from api_files.bibleVerseOfTheDay import get_verse
from api_files.poemOfTheDay import get_poem
from api_files.wordOfTheDay import get_word
from api_files.stock import get_stock_price, get_stock_quote, createGraph
import requests
import time
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt



app = Flask(__name__)


@app.route('/')
# renders homepage
def index():
    return render_template('index.html')


@app.route('/poem')
# gets poem of the day
def get_poem1():
    return get_poem()


@app.route('/verse')
# gets verse of the day
def get_verse1():
    return get_verse()


@app.route('/word')
# gets word of the day
def get_word1():
    return get_word()

@app.route('/stock_price/<name>')
# gets stock price    
def get_price(name):
    return get_stock_price(name)

@app.route('/stock_info/<name>')
# gets stock info    
def get_info(name):
    return get_stock_quote(name)

@app.route('/stock_graph/<name>/<interval>')
# creates graph    
def get_graph(name, interval):
    return createGraph(name, interval)


if __name__ == "__main__":
    app.run(debug=True)