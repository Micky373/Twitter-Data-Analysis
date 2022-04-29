import streamlit as st
import pandas as pd

df = pd.read_csv('./data/clean_processed_tweet_data.csv')

tweet_to_graph = df[['original_text','polarity']]

st.write('# This is the twitter dataset')

df

st.write('# These are some plots')

st.image('https://i.ibb.co/z8qMG2L/plotscrnsht.png')
st.image('https://i.ibb.co/c3zNmsP/plotscrnsht2.png')