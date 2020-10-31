import pandas as pd
import matplotlib.pyplot as plt

CASES = 'Cases'
DEATHS = 'Deaths'

def plot_states(states=['Massachusetts'], days=7, mode=CASES, filename=None):
	COLUMN = 'Province_State'
	df = load_relevant_data(True, mode).groupby(COLUMN).sum().reset_index()
	plot_data(df, states, days, mode, COLUMN, filename)

def plot_countries(countries=['US'], days=7, mode=CASES, filename=None):
	COLUMN = 'Country/Region'
	df = load_relevant_data(False, mode).groupby(COLUMN).sum().reset_index()
	plot_data(df, countries, days, mode, COLUMN, filename)

def load_relevant_data(us_data=True, mode=CASES):
	# This can be changed to your local directory (./) for testing purposes
	#BASE_PATH = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/'
	BASE_PATH = './data/'
	if us_data and mode == CASES:
		PATH = BASE_PATH + 'time_series_covid19_confirmed_US.csv'
	elif us_data and mode == DEATHS:
		PATH = BASE_PATH + 'time_series_covid19_deaths_US.csv'
	elif not us_data and mode == CASES:
		PATH = BASE_PATH + 'time_series_covid19_confirmed_global.csv'
	elif not us_data and mode == DEATHS:
		PATH = BASE_PATH + 'time_series_covid19_deaths_global.csv'

	return pd.read_csv(PATH)

def plot_data(df, places, days, mode, column, filename):
	for place in places:
		cumulative_data = df[df[column] == place]
		counts = cumulative_data.diff(axis=1) # Converts from total case count to daily case count
		x_values = list(counts.columns[-days:])
		y_values = [int(counts[col]) for col in x_values]

		plt.plot(x_values, y_values, label=place)

	label_figure(x_values, y_values, mode, filename)

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