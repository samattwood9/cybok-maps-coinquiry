import streamlit as st
import plotly.graph_objects as go
import pandas as pd

# config + layout
st.set_page_config(page_title="Mapping cyber-enabled roles to CyBOK", page_icon="🗺️")

st.sidebar.write('This dashboard presents cyber-enabled roles mapped to the CyBOK through co-operative inquiry. You can read more about how the mappings were created here: https://www.cybok.org/news/outreach-projects.')
st.sidebar.write('This work was supported by the Cyber Security Body of Knowledge (CyBOK) call for funded Outreach, Adoption, and Awareness projects around CyBOK v1.1. The CyBOK v1.1 is accessible here: https://www.cybok.org/knowledgebase1_1/')
st.sidebar.write('CyBOK © Crown Copyright, The National Cyber Security Centre 2023, licensed under the Open Government Licence: http://www.nationalarchives.gov.uk/doc/open-government-licence/')

st.title("Mapping cyber-enabled roles to CyBOK")

st.write(
    "This app shows cyber-enabled roles mapped to knowledge areas in the Cyber Security Body of Knowledge. The mappings were created through co-operative inquiry with 19 cyber-enabled practitioners. Select a descriptive title that aligns to your job role below to highlight the CyBOK knowledge most relevant to you. More titles will be added in the future."
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
selected_titles = st.multiselect("Select generic job titles to view mappings:", title2mapping.keys(), help="Note: We do not advise comparing the mapped job titles to mapped degree programmes at this time.")

if len(selected_titles) != 0:
    # make plot
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

    st.plotly_chart(fig)
else:
    st.info('Select one title or more to view mappings.')

