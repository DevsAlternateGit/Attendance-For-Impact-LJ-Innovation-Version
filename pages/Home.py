import streamlit as st

# Logo
st.logo("resources\\logo.png", icon_image="resources\\mini_logo.jpg",size='large')

# Image
st.image("resources\\logo.png", use_container_width=True)

"#### Add some info about the app here"

with st.container(border=True):
    "# Something about Generate Analysis "
    # Generate Analysis Button
    st.page_link("Generate_Analysis.py", label="Generate Analysis", icon="📊")  

with st.container(border=True):
    "# Something about View Research Paper "
    # View Research Paper Button
    st.page_link("View_Research_Paper.py", label="View Research Paper", icon="📄")

with st.container(border=True):
    "# Something about Contribution & Repository "
    # View Github Repository Button
    st.link_button("GithHub Repository", "https://github.com/DevsAlternateGit/Student-Analysis", icon="🔗")