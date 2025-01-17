import streamlit as st
from PIL import Image

import inputValidator as iv

# Logo
st.logo("resources\\logo.png", icon_image="resources\\mini_logo.jpg",size='large')

# Title
st.title("Institute Form")

# Session State Variables initailization
if 'next_btn' not in st.session_state:
    st.session_state.next_btn = False

# Callbacks
def change_next_btn_state():
    st.session_state['next_btn'] = True

# Input fields   
with st.container(border=True):
    # Name
    name = st.text_input("Enter your Name")
    iv.validateString(name)

    # Institute Name
    institute_name = st.text_input("Enter your Institute Name")
    iv.validateString(institute_name)

    # Institute Type
    institute_type = st.radio(
        "Institute Type",
        ["School🏫", "College"],
        captions=[
            "1st - 12th Grade",
            "Diploma, Degree, Masters, etc.",
        ],
        horizontal=True,
    )

    # Institute Logo
    institute_logo = st.file_uploader("Upload Institute Logo", type=["png", "jpg", "jpeg"])

    # Check if a file is uploaded
    if institute_logo is not None:
        try:
        # Open and display the image
            image = Image.open(institute_logo)
            st.image(image, caption="Uploaded Institute Logo", use_container_width=True)
            st.success("Logo uploaded successfully!")
        except Exception as e:
            st.error(f"Error processing the file: {e}")

    # Number of Subjects
    num_subjects = st.slider("Number of Subjects", 1, 10,4)

    all_valid = institute_name and name and institute_logo

    # Next button
    st.button(label="Next", disabled=not all_valid, icon="➡️", on_click=change_next_btn_state)  
 
# Subjects      
if st.session_state.next_btn:

    # Subject 1 (minimum 1 subject always true)
    if True:
        with st.popover("Subject 1", icon='1️⃣', use_container_width=True):
            st.header("Subject 1")
            
            # Subject Name
            sub1_name = st.text_input("Enter Subject-1 Name")
            iv.validateString(sub1_name)
    
            # Subject Type
            sub1_type = option = st.selectbox(
                "Subject-1 Type",
                ("Technical", "Mathematical","Science", "Language", "Sports", "Arts", "Others"),
                index=None,
                placeholder="Select Subject-1 type",
            ) 
    
            # Subject Practical
            if sub1_type == "Technical":
                sub1_practical = st.checkbox("Practical")
    
            # Subject File
            sub1_file = st.file_uploader("Upload Subject-1 File", type=["csv","xls","xslx"])

            #

    # Subject 2
    if num_subjects >= 2:
        with st.expander(label="Subject 2", icon='2️⃣'):
            st.header("Subject 2")
            # Subject Name
            sub2_name = st.text_input("Enter Subject-2 Name")
            iv.validateString(sub2_name)

            # Subject Type
            sub2_type = option = st.selectbox(
                "Subject-2 Type",
                ("Technical", "Mathematical","Science", "Language", "Sports", "Arts", "Others"),
                index=None,
                placeholder="Select Subject-2 type",
            ) 

            # Subject Practical
            if sub2_type == "Technical":
                sub2_practical = st.checkbox("Practical")

            # Subject File
            sub2_file = st.file_uploader("Upload Subject-2 File", type=["csv","xls","xslx"])
    
    # Subject 3
    if num_subjects >= 3:
        with st.expander(label="Subject 3", icon='3️⃣'):
            st.header("Subject 3")
            # Subject Name
            sub3_name = st.text_input("Enter Subject-3 Name")
            iv.validateString(sub3_name)

            # Subject Type
            sub3_type = option = st.selectbox(
                "Subject-3 Type",
                ("Technical", "Mathematical","Science", "Language", "Sports", "Arts", "Others"),
                index=None,
                placeholder="Upload Subject-3 Type",
            ) 

            # Subject Practical
            if sub3_type == "Technical":
                sub3_practical = st.checkbox("Practical")

            # Subject File
            sub3_file = st.file_uploader("Upload Subject-3 File", type=["csv","xls","xslx"])
    
    # Subject 4
    if num_subjects >= 4:
        with st.expander(label="Subject 4", icon='4️⃣'):
            st.header("Subject 4")
            # Subject Name
            sub4_name = st.text_input("Enter Subject-4 Name")
            iv.validateString(sub4_name)

            # Subject Type
            sub4_type = option = st.selectbox(
                "Subject-4 Type",
                ("Technical", "Mathematical","Science", "Language", "Sports", "Arts", "Others"),
                index=None,
                placeholder="Upload Subject-4 Type",
            ) 

            # Subject Practical
            if sub4_type == "Technical":
                sub4_practical = st.checkbox("Practical")

            # Subject File
            sub4_file = st.file_uploader("Upload Subject-4 File", type=["csv","xls","xslx"])
    
    # Subject 5
    if num_subjects >= 5:
        with st.expander(label="Subject 5", icon='5️⃣'):
            st.header("Subject 5")
            # Subject Name
            sub5_name = st.text_input("Enter Subject-5 Name")
            iv.validateString(sub5_name)

            # Subject Type
            sub5_type = option = st.selectbox(
                "Subject-5 Type",
                ("Technical", "Mathematical","Science", "Language", "Sports", "Arts", "Others"),
                index=None,
                placeholder="Upload Subject-5 Type",
            ) 

            # Subject Practical
            if sub5_type == "Technical":
                sub5_practical = st.checkbox("Practical")

            # Subject File
            sub5_file = st.file_uploader("Upload Subject-5 File", type=["csv","xls","xslx"])
    
    # Subject 6
    if num_subjects >= 6:
        with st.expander(label="Subject 6", icon='6️⃣'):
            st.header("Subject 6")
            # Subject Name
            sub6_name = st.text_input("Enter Subject-6 Name")
            iv.validateString(sub6_name)

            # Subject Type
            sub6_type = option = st.selectbox(
                "Subject-6 Type",
                ("Technical", "Mathematical","Science", "Language", "Sports", "Arts", "Others"),
                index=None,
                placeholder="Upload Subject-6 Type",
            ) 

            # Subject Practical
            if sub6_type == "Technical":
                sub6_practical = st.checkbox("Practical")

            # Subject File
            sub6_file = st.file_uploader("Upload Subject-6 File", type=["csv","xls","xslx"])
    
    # Subject 7
    if num_subjects >= 7:
        with st.expander(label="Subject 7", icon='7️⃣'):
            st.header("Subject 7")
            # Subject Name
            sub7_name = st.text_input("Enter Subject-7 Name")
            iv.validateString(sub7_name)

            # Subject Type
            sub7_type = option = st.selectbox(
                "Subject-7 Type",
                ("Technical", "Mathematical","Science", "Language & Literature", "Sports", "Arts", "Others"),
                index=None,
                placeholder="Upload Subject-7 Type",
            ) 

            # Subject Practical
            if sub7_type == "Technical":
                sub7_practical = st.checkbox("Practical")

            # Subject File
            sub7_file = st.file_uploader("Upload Subject-7 File", type=["csv","xls","xslx"])
    
    # Subject 8
    if num_subjects >= 8:
        with st.expander(label="Subject 8", icon='8️⃣'):
            st.header("Subject 8")
            # Subject Name
            sub8_name = st.text_input("Enter Subject-8 Name")
            iv.validateString(sub8_name)

            # Subject Type
            sub8_type = option = st.selectbox(
                "Subject Type",
                ("Technical", "Mathematical","Science", "Language", "Sports", "Arts", "Others"),
                index=None,
                placeholder="Upload Subject-8 Type",
            ) 

            # Subject Practical
            if sub8_type == "Technical":
                sub8_practical = st.checkbox("Practical")

            # Subject File
            sub8_file = st.file_uploader("Upload Subject-8 File", type=["csv","xls","xslx"])
    
    # Subject 9
    if num_subjects >= 9:                                         
        with st.expander(label="Subject 9", icon='9️⃣'):
            st.header("Subject 9")
            # Subject Name
            sub9_name = st.text_input("Enter Subject-9 Name")
            iv.validateString(sub9_name)

            # Subject Type
            sub9_type = option = st.selectbox(
                "Subject Type",
                ("Technical", "Mathematical","Science", "Language & Literature", "Sports", "Arts", "Others"),
                index=None,
                placeholder="Upload Subject-9 Type",
            ) 

            # Subject Practical
            if sub9_type == "Technical":
                sub9_practical = st.checkbox("Practical")

            # Subject File
            sub9_file = st.file_uploader("Upload Subject-9 File", type=["csv","xls","xslx"])
    
    # Subject 10
    if num_subjects >= 10:
        with st.expander(label="Subject 10"):
            st.header("Subject 10")
            # Subject Name
            sub10_name = st.text_input("Enter Subject-10 Name")
            iv.validateString(sub10_name)

            # Subject Type
            sub10_type = option = st.selectbox(
                "Subject-10 Type",
                ("Technical", "Mathematical","Science", "Language", "Sports", "Arts", "Others"),
                index=None,
                placeholder="Upload Subject-10 Type",
            ) 

            # Subject Practical
            if sub10_type == "Technical":
                sub10_practical = st.checkbox("Practical")

            # Subject File
            sub10_file = st.file_uploader("Upload Subject-10 File", type=["csv","xls","xslx"])
        
