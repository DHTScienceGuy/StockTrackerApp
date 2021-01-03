# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 20:21:08 2021

@author: The Art Of DHT
"""

import yfinance as yf
import streamlit as st
import pandas as pd 

st.write("""
         
         #Simple Stock Price App
         Shown are the stock closing price
         and volume of company
         
         """)
         
""" Getting Price of Company Stock """

tickerSymbol = 'TWX'

# Ticker Data ticker output

tickerData = yf.Ticker(tickerSymbol)

# get historical price

tickerDf = tickerData.history(period='id', start='2010-5-31', end='2020-5-31')

#open high, Low Close, Volume, Dividends, Stock Splits

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
 