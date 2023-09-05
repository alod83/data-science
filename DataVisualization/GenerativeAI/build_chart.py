# import the required libraries
# load the data 'tsc00001.csv' into a pandas dataframe
# drop the 'unit' column
# select the rows where 'geo' is 'IT'
# drop the 'geo' column
# use melt() as follows:
# - use 'sectperf' as id_vars
# - use 'date' as var_name
# - use 'value' as value_name
# convert the 'date' column to integer
# convert the 'value' column to float

# draw a line chart in Python Altair as follows:
# - use 'data' for the x axis
# - use the value column for the y axis
# - use 'sectperf' for color
# save the chart as 'chart.html'

import pandas as pd
import altair as alt

df = pd.read_csv('tsc00001.csv')
df = df.drop(columns=['unit'])
df = df[df['geo'] == 'IT']
df = df.drop(columns=['geo'])
df = pd.melt(df, id_vars=['sectperf'], var_name='date', value_name='value')
df['date'] = df['date'].astype(int)
df['value'] = df['value'].astype(float)

chart = alt.Chart(df).mark_line().encode(
    x=alt.X('date:O', title='', axis=alt.Axis(labelAngle=0)),
    y=alt.Y('value', title='Percentage of gross domestic product'),
    color=alt.Color('sectperf', legend=None),
    # set the StrokeWith as follows:
    # - if 'sectperf' is 'BES', use 5
    # - in the other cases use 1
    strokeWidth=alt.condition(
        alt.datum.sectperf == 'BES',
        alt.value(5),
        alt.value(1)
    )
).properties(
    width=600,
    height=400,
    title=['Driving Growth:',
        'A Decade of Business Enterprise Performance Dominance (2010-2021)']
)

# add a text layer as follows:
# - select only date == 2021
# - use 'data' for the x axis
# - use the sectperf column for the y axis

text = alt.Chart(df[df['date'] == 2021]).mark_text(
    align='left',
    baseline='middle',
    dx=7,
    fontSize=14
).encode(
    x=alt.X('date:O', title='', axis=alt.Axis(labelAngle=0)),
    y=alt.Y('value', title='Percentage of gross domestic product'),
    text='sectperf',
    color=alt.Color('sectperf', legend=None),
).properties(
    width=600,
    height=400,
)

# Add the following image to the chart: 'red.png'

df_red = pd.DataFrame({'url': ['red.png']})

red = alt.Chart(df_red).mark_image(
    align='center',
    baseline='top',
    width=300,
    height=300
).encode(
    url='url'
)



chart = (red | chart + text 
).configure_axis(
    grid=False,
    titleFontSize=14,
).configure_view(
    strokeWidth=0
).configure_title(
    fontSize=20,
    anchor='middle',
    color='grey'
)

chart.save('chart.html')