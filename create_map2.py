import pycountry
import pandas as pd
import plotly.express as px
from us_state_abbrev import us_state_abbrev

df_confirm = pd.read_csv('time_series_covid19_confirmed_US.csv')

print(df_confirm.head())

#df_confirm = df_confirm.drop(columns=['Province/State', 'Lat', 'Long'])
#df_confirm = df_confirm.drop()
date_list = list(df_confirm.columns)
df_confirm = df_confirm.groupby('Province_State')[date_list].agg('sum')


df_confirm['state'] = [us_state_abbrev.get(x, None) for x in list(df_confirm.index)]
df_confirm['total'] = df_confirm.diff(axis=1)["9/10/20"]

print(df_confirm.head())


fig = px.choropleth(df_confirm,
                     locations="state",
                     locationmode="USA-states",
                     scope="usa",          # identify country code column
                     color="total",                  # identify representing column
                     hover_name="state",              # identify hover name
                     #projection="orthographic",        # select projection
                     color_continuous_scale = 'Peach',  # select prefer color scale           # select range of dataset
                     )

fig.show()
fig.update_layout(margin=dict(l=0, r=0, t=0, b=0))
fig.write_image('./map.png', engine='kaleido')