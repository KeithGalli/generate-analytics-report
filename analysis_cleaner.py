import pandas as pd
import matplotlib.pyplot as plt

def retrieve_state_data(states=['Massachusetts'], days=7, mode='cases'):
	if mode=='Cases':
		df = load_USA_time_series_data().groupby('Province_State').sum().reset_index()
	else:
		df = load_USA_deaths().groupby('Province_State').sum().reset_index()

	for state in states:
		state_data = df[df['Province_State'] == state]
		state_time_series = state_data.diff(axis=1)

		x_values = list(state_time_series.columns[-days:])
		y_values = [int(state_time_series[col]) for col in x_values]

		plt.plot(x_values, y_values, label=state)

	graph_time_series_data(x_values, y_values, state, mode)

def graph_time_series_data(x_values, y_values, state, mode):
	days = len(x_values)
	plt.title(f'Daily {mode}, Last {days} Days')
	skip = max(len(x_values)//4, 1) # Helps ensure we don't add too many date tick marks
	plt.xticks(x_values[::skip])
	plt.xlabel("Date (MM/DD/YY)")
	plt.ylabel(f"{mode}")
	plt.legend()
	plt.savefig(f'last_{days}_{mode}.png')
	plt.show()


def load_USA_time_series_data():
	#URL = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv'
	URL = 'time_series_covid19_confirmed_US.csv'
	return pd.read_csv(URL)

def load_USA_deaths():
	URL = 'time_series_covid19_deaths_US.csv'
	return pd.read_csv(URL)


states = ['Massachusetts', 'New Hampshire']
retrieve_state_data(states, 250, 'Cases')
