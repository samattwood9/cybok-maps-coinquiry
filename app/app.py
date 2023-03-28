import streamlit as st
import plotly.graph_objects as go
import plotly.offline as pyo
import pandas as pd
import numpy as np

import plotly.express as px


st.set_page_config(page_title="Mapping cyber-enabled roles to CyBOK", page_icon="🗺️", layout="wide")

st.title("Mapping cyber-enabled roles to CyBOK")

st.write(
    "This app shows cyber-enabled roles mapped to knowledge areas in the Cyber Security Body of Knowledge. The mappings were created through cooperative inquiry with cyber-enabled practitioners."
)
# user selection
titles = ["Holder 1", "Holder 2", "Holder 3"]
st.multiselect("Select generic job titles to view mappings:", titles)

# display mapping - spider/groups
col1, col2, col3 = st.columns([6, 1, 6])

vals = [1, 2, 3, 3, 2, 1]
categories = ['One', 'Two', 'Three', 'Four', 'Five', 'One']

fig = go.Figure(
    data=[
        go.Scatterpolar(r=vals, theta=categories, name='Holder 1', line_width=5, marker_size=12),
    ],
    layout=go.Layout(
        title=go.layout.Title(text='Mapping to knowledge groups'),
        polar={'radialaxis': {'visible': True}},
        showlegend=True
    )
)

col1.plotly_chart(fig)

# display mapping - recommended KAs
col3.write('Based on the selected titles, we think these knowledge areas are the most relevant:')

col3.write(':one: Example area')

col3.write(':two: Example area')

col3.write(':three: Example area')

col3.write(':four: Example area')

col3.write(':five: Example area')

col3.write('To learn more and access resources related to these knowledge areas, visit the CyBOK v1.1: https://www.cybok.org/knowledgebase1_1/.')

