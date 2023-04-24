import streamlit as st
import plotly.graph_objects as go
import plotly.offline as pyo
import pandas as pd
import numpy as np

# config + layout
st.set_page_config(page_title="Mapping cyber-enabled roles to CyBOK", page_icon="🗺️", layout="wide")

st.title("Mapping cyber-enabled roles to CyBOK")

st.write(
    "This app shows cyber-enabled roles mapped to knowledge areas in the Cyber Security Body of Knowledge. The mappings were created through cooperative inquiry with cyber-enabled practitioners."
)

# load data
mappings_df = pd.read_csv('./data/mappings.csv', index_col=False)

categories = mappings_df.columns.values.tolist()[1:]
categories.append(categories[0])

title2mapping = {}
for _, row in mappings_df.iterrows():
    title2mapping[row['Title']] = [
        row['Human Organisational & Regulatory Aspects'],
        row['Attacks & Defences'],
        row['Systems Security'],
        row['Software & Platform Security'],
        row['Infrastructure Security'],
        row['Human Organisational & Regulatory Aspects'] # repeat for spider diagram
    ]

# user selection
selected_titles = st.multiselect("Select generic job titles to view mappings:", title2mapping.keys())

# display mapping - spider/groups
col1, col2, col3 = st.columns([6, 1, 6])

#vals = [1, 2, 3, 3, 2, 1]
#categories = ['Human Organisational & Regulatory Aspects', 'Attacks & Defences', 'Systems Security', 'Software & Platform Security', 'Infrastructure Security', 'Human Organisational & Regulatory Aspects']

mapping_data = []
for selected_title in selected_titles:
    mapping_data.append(go.Scatterpolar(r=title2mapping[selected_title], theta=categories, name=selected_title, line_width=5, marker_size=12))

fig = go.Figure(
    data=mapping_data,
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

