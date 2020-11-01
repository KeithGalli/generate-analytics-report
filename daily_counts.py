# Python Libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Local files
from helper import Mode, load_relevant_data

TEST_DATE = "10/20/20"

def plot_daily_count_states(states=['Massachusetts'], day=TEST_DATE, mode=Mode.CASES, filename=None):
	COLUMN = 'Province_State'
	df = load_relevant_data(True, mode).groupby(COLUMN).sum().reset_index()
	plot_data(df, states, day, mode, COLUMN, filename)

def plot_daily_count_countries(countries=['US'], day=TEST_DATE, mode=Mode.CASES, filename=None):
	COLUMN = 'Country/Region'
	df = load_relevant_data(False, mode).groupby(COLUMN).sum().reset_index()
	plot_data(df, countries, day, mode, COLUMN, filename)

def plot_data(df, places, day, mode, column, filename):
	n = len(places)
	colors = plt.cm.Reds(np.linspace(0.35,0.65,n))

	values = []
	for index, place in enumerate(places):
		cumulative_data = df[df[column] == place]
		start_column = cumulative_data.columns.get_loc("1/22/20")
		counts = cumulative_data.iloc[:, start_column:].diff(axis=1) # Converts from total case count to daily case count
		values.append(int(counts[day]))

	plt.bar(places, values, color=colors)
	label_figure(day, mode, filename)
	
def label_figure(day, mode, filename):
	plt.title(f'{mode}, {day}')
	plt.ylabel(f"{mode}")
	filename = filename if filename else f'{mode}_{day.replace("/", "-")}.png'
	plt.savefig(filename)
	plt.close()

if __name__ == '__main__':
	
	states = ["Massachusetts", "New Hampshire", "Rhode Island"]
	plot_daily_count_states(states, day="10/10/20")
	plot_daily_count_states(states, mode=Mode.DEATHS)

	plot_daily_count_countries(["India", "US", "Brazil"])

