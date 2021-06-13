import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.

import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

#st.title('hehe duar duar ')

#tickers = "WIKA.JK"

st.write(f""" 
# Simple Stock Price App

""")

#tickers = ''

#status = st.radio("")

user_input = st.sidebar.text_input("Enter stock code: ",'BBCA')

st.write(f"""Shown are the **stock closing** and **volume** of **{user_input}**
""")

tickerData = yf.Ticker(user_input+".JK")

tickerDf = tickerData.history(period='1d',start='2010-1-1')


st.write("""## Closing Price""")

close_chart = px.line(tickerDf, y="Close")
st.plotly_chart(close_chart)

st.write("""## Volume""")

volume_chart = px.line(tickerDf, y="Close")
st.plotly_chart(volume_chart)

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data


#option = st.selectbox(
    #'Which number do you like best?',
    # df['first column'])

#'You selected: ', option


option = st.sidebar.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected:', option


left_column, right_column = st.beta_columns(2)
pressed = left_column.button('Press me?')
if pressed:
    right_column.write("Woohoo!")

expander = st.beta_expander("FAQ")
expander.write("Here you could put in some really, really long explanations...")

st.help(plotly_chart)


