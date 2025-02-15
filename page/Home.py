import streamlit as st

# Logo
image = "resources\\logo.png"
st.logo(image, size='large')

# Image
st.image(image, use_container_width=True)

"#### This is an app designed to help institutions refine their policies and gain deeper insights into academic performance, revealing hidden patterns through thoughtful analysis and guidance."

with st.container(border=True):
    """ # Bridging Research and Application
    This app is built upon the principles explored in the study "Attendance for Impact."
    The insights from this research take form in practice, transforming theory into application, refining policies, and unveiling deeper patterns within academic performance."""
    # View Research Paper Button
    st.page_link("page\\View_Research_Paper.py", label="View Research Paper", icon="📄")

with st.container(border=True):
    "# Generate Analysis "
    "###### Enter the details of your institution and get a detailed analysis of student performance."
    # Generate Analysis Button
    st.page_link("page\\Generate_Analysis.py", label="Generate Analysis", icon="📊")  

with st.container(border=True):
    "# Contribution & Repository"  
    # View GitHub Repository Button  
    st.link_button("View Project on GitHub", "https://github.com/ShailKPatel/Attendance_For_Impact", icon="🔗")