# Python libraries
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta

# Local files
from helper import load_relevant_data, us_state_abbrev

def plot_usa_case_map(filename=None, day=None):
	df = load_relevant_data()
	dates = list(df.columns)
	df = df.groupby('Province_State')[dates].agg('sum')
	create_usa_figure(df, filename, day)

def plot_global_case_map(filename=None, day=None):
	df = load_relevant_data(us_data=False)
	dates = list(df.columns)
	df = df.groupby('Country/Region')[dates].agg('sum')
	create_global_figure(df, filename, day)

def create_usa_figure(df, filename, day):
	day = day if day else yesterday # default to yesterday's date if not provided

	df['Cases'] = df.diff(axis=1)[day]
	df['state'] = [us_state_abbrev.get(x, None) for x in list(df.index)]
	

	fig = px.choropleth(df,
                    locations="state",
                    locationmode="USA-states",
                    scope="usa",
                    color="Cases",
                    hover_name="state",
                    color_continuous_scale='Peach',
                    title=f"US Daily Cases, {day}",
                    width=1000,
                    #height=500,
                    range_color=[0,3000])

	fig.update_layout(margin=dict(l=0, r=0, t=70, b=0), title={"font": {"size": 20}, "x":0.5},)
	filename = filename if filename else "usa_chart.png"
	fig.write_image(filename, engine='kaleido')

def create_global_figure(df, filename, day):
	day = day if day else yesterday # default to yesterday's date if not provided

	df['Cases'] = df.diff(axis=1)[day]
	df['Country'] = df.index

	fig = px.choropleth(df,
                    locations="Country",
                    locationmode="country names",
                    scope="world", # Try 'europe', 'africa', 'asia', 'south america', 'north america'
                    color="Cases",
                    hover_name="Country",
                    #projection="miller",
                    color_continuous_scale='Peach',
                    title=f"Global Daily Cases, {day}",
                    width=1000,
                    #height=500,
                    range_color=[0,50000])

	fig.update_layout(margin=dict(l=0, r=0, t=70, b=20), title={"font": {"size": 20}, "x":0.5},)
	filename = filename if filename else "global_chart.png"
	fig.write_image(filename, engine='kaleido')

if __name__ == '__main__':
	yesterday = (datetime.today() - timedelta(days=1)).strftime("%m/%d/%y")
	# Uncomment below line for testing
	yesterday = "10/10/20"

	plot_usa_case_map(day=yesterday) # saves as usa_chart.png by default
	plot_global_case_map(day=yesterday) # saves as global_chart.png by default