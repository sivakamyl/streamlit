# pip install ydata-profiling 
# NOT streamlit_pandas_profiling

import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

st.header('`streamlit_pandas_profiling`')

#df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
df = pd.read_csv(r'orgs.csv')
st.write(df)
profile = ProfileReport(df, title="Profiling Report")
print(profile)
#pr = df.profile_report()
st_profile_report(profile)