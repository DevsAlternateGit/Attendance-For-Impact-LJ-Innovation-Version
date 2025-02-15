import streamlit as st

home = st.Page("page\\Home.py", icon='🏠')

view_research_paper = st.Page("page\\View_Research_Paper.py", icon='📄')

generate_analysis = st.Page("page\\Generate_Analysis.py", icon='📊')

credits = st.Page("page\\Credits.py", icon='📇')


pg = st.navigation({
    "Home": [home],
    "Research Paper": [view_research_paper],
    "Analysis": [generate_analysis],
    "Credits": [credits]
})
pg.run()
