import streamlit as st
import pandas as pd

st.title("Streamlit Inputs")

# SIDEBAR OF THE APP
add_radio = None
with st.sidebar:
    add_radio = st.radio("Choose a page you want!", ("Input Data", "Excel Input"))

    st.divider()
    st.write(add_radio)

# MAIN CONTENT OF THE APP
if add_radio == "Input Data":
    name = st.text_input(label="Your name:")
    age = st.number_input(label="Your age:", min_value=0, max_value=200, step=1)
    is_married = st.checkbox(label="Are you married?")
    genre = st.radio(
        "What's your favorite movie genre",
        [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
    )
    options = st.multiselect(
        label="What are your favorite colors",
        options=["Green", "Yellow", "Red", "Blue", "Magenta", "Brown"],
        default=["Yellow", "Red"],
    )
    motto = st.text_area(label="Your motto")

    if st.button(label="Process", type="primary", disabled=True):
        st.write(f"Your name is {name}, and your age is {age}.")
        married = "married" if is_married else "not married"
        st.write(f"Your marital status is {married}.")
        st.write(f"Your favorite movie genre is {genre}")
        st.write(f"Your favorite colors are {options}")
        st.write(f"Your motto is {motto}")


if add_radio == "Excel Input":
    uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx"])

    if uploaded_file is not None:
        try:
            df = pd.read_excel(uploaded_file)
            st.subheader("Data from the Excel file:")
            st.dataframe(df, hide_index=True)  # Using st.dataframe
        except Exception as e:
            st.error(f"Error reading the Excel file: {e}")
    else:
        st.info("Please upload an Excel file to view its contents.")
