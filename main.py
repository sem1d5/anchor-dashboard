import streamlit as st 
import pandas as pd 
import plotly.express as px
import numpy as np 

header = st.container()
total_users = st.container()
daily_activity = st.container()
ust_wallet = st.container()

with header:
	st.title('Premium Anchor Dashboard')
	st.text('example text')

with total_users:
	st.header('Number of users on Anchor')
	st.text('example text')

	#mau_data = pd.read_csv('data/mau_anchor.csv')


	#st.table(mau_data)

	#mau_data = pd.DataFrame({'mau_anchor':columns=['months', 'monthly_active_users']})
	#mau_data['mau_anchor'] = mau_data['mau_anchor'].astype(str)
	
	#csv_file = 'mau_anchor.csv',sheetnames = 'DATA'

	df = pd.read_excel('data/mau_anchor.xlsx', sheet_name = 'data',usecols = 'A:B', header = 0)

	st.dataframe(df)

	mau_bar = px.bar(df, title = 'test title', x = 'MONTHS', y = 'MONTHLY_ACTIVE_USERS')

	st.plotly_chart(mau_bar)


with daily_activity:
	st.header('Daily activity')
	st.text('example text')


with ust_wallet:
	st.header('Wallet deposit growth')
	st.text('example text')








