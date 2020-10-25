import pandas as pd
import matplotlib.pyplot as plt

def retrieve_state_data(state='Massachusetts', days=7, color='b'):
	df = load_USA_time_series_data().groupby('Province_State').sum().reset_index()
	state_data = df[df['Province_State'] == state]
	state_time_series = state_data.diff(axis=1)

	x_values = list(state_time_series.columns[-days:])
	y_values = [int(state_time_series[col]) for col in x_values]

	graph_time_series_data(x_values, y_values, state, color)

def graph_time_series_data(x_values, y_values, state, color='b'):
	days = len(x_values)
	plt.title(f'Daily Cases, Last {days} Days')
	plt.plot(x_values, y_values, label=state, color=color)
	skip = max(len(x_values)//5, 1) # Helps ensure we don't add too many date tick marks
	plt.xticks(x_values[::skip])
	plt.xlabel("Date (MM/DD/YY)")
	plt.ylabel("Cases")
	plt.legend()
	plt.savefig(f'{state}_{days}.png')
	plt.show()


def load_USA_time_series_data():
	#URL = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv'
	URL = 'time_series_covid19_confirmed_US.csv'
	return pd.read_csv(URL)

retrieve_state_data('New Hampshire', 7, color='orange')
retrieve_state_data('New Hampshire', 30, color='orange')
retrieve_state_data('Massachusetts', 7)
retrieve_state_data('Massachusetts', 30)