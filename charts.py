import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

df1 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df1).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)

line_chart = st.line_chart(df1)

df = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.area_chart(df)
st.bar_chart(df)

#graphViz
#dagre-d3 library
import graphviz
st.graphviz_chart('''
    digraph {
        eat -> sleep
        sleep -> repeat
        repeat -> eat
    }
''')
# pip install streamlit-apex-charts