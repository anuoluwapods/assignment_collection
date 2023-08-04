import streamlit as st
from PIL import Image
from deta import Deta
import re
# Initialize Deta instance
deta = Deta(st.secrets["deta_key"])
user_db = deta.Base('assignment_collection')

# Streamlit app
def main():
    st.title("Modern Streamlit App")
    st.markdown(
        """
        <style>
        .container {
            margin: 0 auto;
            max-width: 800px;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
            font-family: Arial, sans-serif;
        }
        .header {
            font-size: 24px;
            margin-bottom: 20px;
        }
        .input-label {
            font-weight: bold;
        }
        .input-field {
            width: 100%;
            padding: 10px;
            margin-bottom: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        .select-field {
            width: 100%;
            padding: 10px;
            margin-bottom: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        .submit-button {
            background-color: #007BFF;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .success-message {
            color: green;
            margin-top: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Container for the image
    image = Image.open('image.png')
    st.image(image, use_column_width=True)

    # Main content container
    main_container = st.container()

    # Left column
    with main_container:
        st.markdown("<div class='container'>", unsafe_allow_html=True)
        st.markdown("<div class='header'>User Information</div>", unsafe_allow_html=True)

        # Input fields
        name = st.text_input("Name", key='name')
        email = st.text_input("Email", key='email')
        cohort = st.text_input("Cohort", key='cohort')
        course_type = st.selectbox("Course Type", ["Select Option","Excel","Python",  "PowerBI", "Tableau", "SQL", "Word File"], key='course_type')

        # File upload
        uploaded_file = st.file_uploader("Upload File (Word Document, Python Notebook, PowerBI, Excel, Tableau, Text File)", type=["docx", "ipynb", "pbix", "xlsx", "twb", "txt"])

        # Submit button
        if st.button("Submit", key='submit_button'):
            if name and email and cohort and course_type:
                # Store user information
                user_data = {
                    "name": name,
                    "email": email,
                    "cohort": cohort,
                    "course_type": course_type
                }
                
                if uploaded_file is not None:
                    user_data["file_name"] = uploaded_file.name
                    user_data["file_data"] = uploaded_file.read()

                user_db.put(user_data)
                st.markdown("<div class='success-message'>User information submitted successfully!</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
