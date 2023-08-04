import streamlit as st
from deta import Deta
import base64

# Initialize Deta instance
deta = Deta(st.secrets["deta_key"])
user_db = deta.Base('assignment_collection')
user_drive = deta.Drive('assignment')

# Streamlit app
def main():
    st.title("Modern Streamlit App")
    st.markdown(
        """
        <!-- Your CSS styles here -->
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
                    # Save the uploaded file to Deta drive
                    file = user_drive.put(uploaded_file)
                    user_data["file_name"] = uploaded_file.name
                    user_data["file_url"] = file.url

                user_db.put(user_data)
                st.markdown("<div class='success-message'>User information submitted successfully!</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
