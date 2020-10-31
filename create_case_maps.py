# Python libraries
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta

# Local files
from us_state_abbrev import us_state_abbrev
from time_series_analysis import load_relevant_data


yesterday = (datetime.today() - timedelta(days=1)).strftime("%m/%d/%y")
# Uncomment below line for testing
#yesterday = "10/10/20"

def plot_usa_case_map(filename=None):
	df = load_relevant_data()
	dates = list(df.columns)
	df = df.groupby('Province_State')[dates].agg('sum')
	create_usa_figure(df, filename)

def plot_global_case_map(filename=None):
	df = load_relevant_data(us_data=False)
	dates = list(df.columns)
	df = df.groupby('Country/Region')[dates].agg('sum')
	create_global_figure(df, filename)

def create_usa_figure(df, filename):

	df['state'] = [us_state_abbrev.get(x, None) for x in list(df.index)]
	df['Cases'] = df.diff(axis=1)[yesterday]

	fig = px.choropleth(df,
                    locations="state",
                    locationmode="USA-states",
                    scope="usa",
                    color="Cases",
                    hover_name="state",
                    color_continuous_scale='Peach',
                    title=f"US Daily Cases, {yesterday}",
                    width=1000,
                    #height=500,
                    range_color=[0,3000])

	fig.update_layout(margin=dict(l=0, r=0, t=70, b=0), title={"font": {"size": 20}, "x":0.5},)
	# fig.show()
	filename = filename if filename else "usa_chart.png"
	fig.write_image(filename, engine='kaleido')

def create_global_figure(df, filename):

	df['Country'] = df.index
	df['Cases'] = df.diff(axis=1)[yesterday]

	fig = px.choropleth(df,
                    locations="Country",
                    locationmode="country names",
                    scope="world", # Try 'europe', 'africa', 'asia', 'south america', 'north america'
                    color="Cases",
                    hover_name="Country",
                    #projection="miller",
                    color_continuous_scale='Peach',
                    title=f"Global Daily Cases, {yesterday}",
                    width=1000,
                    #height=500,
                    range_color=[0,50000])

	fig.update_layout(margin=dict(l=0, r=0, t=70, b=20), title={"font": {"size": 20}, "x":0.5},)
	# fig.show()
	filename = filename if filename else "global_chart.png"
	fig.write_image(filename, engine='kaleido')

plot_usa_case_map()
plot_global_case_map()