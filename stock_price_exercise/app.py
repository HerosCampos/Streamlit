import streamlit as st
import pandas as pd
import yfinance as yf # pip install yfinance

st.markdown("""
    # Simple Stock Price App
    Shown are the stock closing price and volume of Google
""")

tickerData = yf.Ticker('TSLA')

ticker_df = tickerData.history(period = '1w', start = '2020-5-31', end = '2021-5-31')

st.line_chart(ticker_df['Close'])
st.line_chart(ticker_df['Volume'])

















































