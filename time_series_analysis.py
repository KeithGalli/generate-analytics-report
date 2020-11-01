# Python libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Local files
from helper import Mode, load_relevant_data

def plot_states(states=['Massachusetts'], days=7, mode=Mode.CASES, filename=None, end_date=None):
	COLUMN = 'Province_State'
	df = load_relevant_data(True, mode).groupby(COLUMN).sum().reset_index()
	plot_data(df, states, days, mode, COLUMN, filename, end_date)

def plot_countries(countries=['US'], days=7, mode=Mode.CASES, filename=None, end_date=None):
	COLUMN = 'Country/Region'
	df = load_relevant_data(False, mode).groupby(COLUMN).sum().reset_index()
	plot_data(df, countries, days, mode, COLUMN, filename, end_date)

def plot_data(df, places, days, mode, column, filename, end_date):
	n = len(places)
	colors = plt.cm.Oranges(np.linspace(0.35,0.65,n))

	offset = get_end_date_offset(df, end_date) if end_date else 0

	for index, place in enumerate(places):
		cumulative_data = df[df[column] == place]
		start_column = cumulative_data.columns.get_loc("1/22/20")
		counts = cumulative_data.iloc[:, start_column:].diff(axis=1) # Converts from total case count to daily case count
		x_values = list(counts.columns[-days-offset:len(counts.columns)-offset])
		y_values = [int(counts[col]) for col in x_values]

		plt.plot(x_values, y_values, label=place, color=colors[index], linewidth=2)

	label_figure(x_values, y_values, mode, filename)

def get_end_date_offset(df, end_date):
	date_format =  "%m/%d/%y"
	end = datetime.strptime(end_date, date_format)
	last_column = datetime.strptime(df.columns[-1], date_format)
	offset = max(0, (last_column-end).days)
	return offset


def label_figure(x_values, y_values, mode, filename):
	days = len(x_values)
	plt.title(f'Daily {mode}, Last {days} Days')
	skip = max(len(x_values)//5, 1) # Helps ensure we don't add too many date tick marks
	plt.xticks(x_values[::skip])
	plt.xlabel("Date (MM/DD/YY)")
	plt.ylabel(f"{mode}")
	plt.legend()
	filename = filename if filename else f'{mode}_last_{days}.png'
	plt.savefig(filename)
	plt.close()

if __name__ == '__main__':
	plot_states(filename="state-line-chart-test.png")

	countries = ["US", "India", "Brazil"]
	plot_countries(countries, days=100, filename="country-line-chart-test.png")