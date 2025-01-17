import streamlit as st

pg = st.navigation([
                st.Page("Home.py", icon='🏠'), 
                st.Page("Generate_Analysis.py", icon='📊'), 
                st.Page("View_Research_Paper.py", icon='📄'),
])
pg.run()