#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import altair as alt
import streamlit as st
import time

df = pd.read_csv('../sources/tourist_arrivals.csv')
df['date'] = pd.to_datetime(df['date'])

# Build an empty graph
lines = alt.Chart(df).mark_line().encode(
  x=alt.X('1:T',axis=alt.Axis(title='date')),
  y=alt.Y('0:Q',axis=alt.Axis(title='value'))
  ).properties(
      width=600,
      height=300
  )

# Plot a Chart
def plot_animation(df):
    lines = alt.Chart(df).mark_line().encode(
    x=alt.X('date:T', axis=alt.Axis(title='date')),
    y=alt.Y('value:Q',axis=alt.Axis(title='value')),
    ).properties(
        width=600, 
        height=300
    )
    return lines


N = df.shape[0] # number of elements in the dataframe
burst = 6       # number of elements (months) to add to the plot
size = burst    # size of the current dataset

# Plot Animation
line_plot = st.altair_chart(lines)
start_btn = st.button('Start')

if start_btn:
    for i in range(1,N):
        step_df = df.iloc[0:size]       
        lines = plot_animation(step_df)
        line_plot = line_plot.altair_chart(lines)
        size = i + burst
        if size >= N:
            size = N - 1  
        time.sleep(0.1)
