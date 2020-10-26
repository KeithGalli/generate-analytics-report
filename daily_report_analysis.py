import pandas as pd
from datetime import datetime, timedelta

def load_data(us_data=True):
	BASE_PATH = "./"
	#BASE_PATH = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/'
	folder = 'csse_covid_19_daily_reports_us/' if us_data else 'csse_covid_19_daily_reports/'

	yesterday_str, two_days_ago_str = get_past_two_days()
	
	yesterday_file = BASE_PATH + folder + yesterday_str + '.csv'
	yesterday_df = pd.read_csv(yesterday_file)

	two_days_ago_file = BASE_PATH + folder + two_days_ago_str + '.csv'
	two_days_ago_df = pd.read_csv(two_days_ago_file)

	return (yesterday_df, two_days_ago_df)

def get_past_two_days():
	today = datetime.today()
	today_str = today.strftime("%m-%d-%Y")

	yesterday = today - timedelta(days=1)
	yesterday_str = yesterday.strftime("%m-%d-%Y")

	two_days_ago = today - timedelta(days=2)
	two_days_ago_str = two_days_ago.strftime("%m-%d-%Y")

	return (yesterday_str, two_days_ago_str)

def format_df():
	yesterday_df, two_days_ago_df = load_data()

	yesterday_df['New Cases'] = yesterday_df['Confirmed'] - two_days_ago_df['Confirmed']
	yesterday_df["Incident Rate (%)"] = yesterday_df["Incident_Rate"]/100000 * 100
	yesterday_df["Mortality Rate (%)"] = yesterday_df["Mortality_Rate"]/100000 * 100

	return yesterday_df



def get_state_data(states):
	df = format_df()

	## Get single row, append
	df = df[df['Province_State'].isin(states)]

	data = []
	for index, row in df.iterrows():
		data.append(list(row[['Province_State', 'New Cases', 'Incident Rate (%)', 'Mortality Rate (%)']]))


	print(data)


	print(list(df.iloc[0][['Incident_Rate', 'Mortality_Rate']]))

get_state_data(['New Hampshire', 'Massachusetts'])






# df = pd.read_csv(PATH)
# df["Incident Rate (%)"] = df["Incident_Rate"]/100000 * 100
# df["Mortality Rate (%)"] = df["Mortality_Rate"]/100000 * 100
# print(df[df['Province_State'].isin(['New Hampshire', 'Massachusetts'])][['Province_State', 'Incident Rate (%)', 'Mortality Rate (%)']])