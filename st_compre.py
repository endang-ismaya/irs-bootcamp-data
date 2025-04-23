import streamlit as st
import pandas as pd

st.title("Learn Comprehensions")

families = ["ayah", "ibu", "kakak", "adek", "tetangga"]
ages = [32, 28, 8, 2, 33]

dt_families_ages = {name: age for name, age in zip(families, ages)}

df = pd.DataFrame(dt_families_ages, index=[0])
st.dataframe(df)

st.write(dt_families_ages)

chart_data = pd.DataFrame(dt_families_ages, index=[0, 1, 2, 3])
st.line_chart(chart_data)

# st.area_chart(df)
