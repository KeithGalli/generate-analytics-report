import pycountry
import pandas as pd
import plotly.express as px

df_confirm = pd.read_csv('time_series_covid19_confirmed_global.csv')

#df_confirm = df_confirm.drop(columns=['Province/State', 'Lat', 'Long'])
df_confirm = df_confirm.drop(columns=['Province/State'])
date_list = list(df_confirm.columns)
df_confirm = df_confirm.groupby('Country/Region')[date_list].agg('sum')



# Get the three-letter country codes for each country
def get_country_code(name):
    try:
        return pycountry.countries.lookup(name).alpha_3
    except:
        return None

df_confirm['country'] = df_confirm.index
df_confirm['iso_alpha_3'] = df_confirm['country'].apply(get_country_code)

print(df_confirm.head())


fig = px.choropleth(df_confirm,
                     locations="country",
                     locationmode="country names",           # identify country code column
                     color="10/24/20",                  # identify representing column
                     hover_name="country",              # identify hover name
                     projection="orthographic",        # select projection
                     color_continuous_scale = 'Peach',  # select prefer color scale
                     #range_color=[0,50000]              # select range of dataset
                     )

fig.show()
fig.update_layout(margin=dict(l=0, r=0, t=0, b=0))
fig.write_image('./map.png', engine='kaleido')