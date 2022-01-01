import streamlit as st 
import pandas as pd 
import plotly.express as px
import numpy as np 
import plotly.figure_factory as ff

header = st.container()
total_users = st.container()
daily_activity = st.container()
ust_wallet = st.container()

with header:
	st.title('Premium Anchor Dashboard')
	st.text('example text')

with total_users:
	st.header('Number of users on Anchor')
	#st.text('example text')

	#this shows the 3 column metrics 
	col1, col2, col3 = st.columns(3)
	col1.metric("Total Anchor Users", "135k", "1.2 °F")
	col2.metric("Total Borrowers", "40k")
	col3.metric("Total Depositors", "119k")



	#this part reads and shows the table 
	df = pd.read_excel('mau_anchor.xlsx', sheet_name = 'data',usecols = 'A:B', 
						header = 0)

	st.dataframe(df)

	#creates the bar graph 
	mau_bar = px.bar(df, title = 'test title', x = 'MONTHS', y = 'MONTHLY_ACTIVE_USERS')

	st.plotly_chart(mau_bar)

	#inserting DAU data 
	df = pd.read_excel('dau_anchor.xlsx', sheet_name = 'Sheet 1', usecols = 'A:B',
						header = 0)
	st.dataframe(df)

	#creates line graph for DAU 
	dau_fig = px.line(df, title = 'dau title',x = 'DATES', y = 'DAILY_ACTIVE_USERS')
	dau_fig.show()



with daily_activity:
	st.header('Daily activity')
	st.text('example text')


with ust_wallet:
	st.header('Wallet deposit growth')
	st.text('example text')








