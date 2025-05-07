import streamlit as st

st.title("IRS Data Input")

FILEPATH = "irs_data.txt"

# placeholder
ph = st.empty()

# columns space
col1, col2, col3 = st.columns([2, 7, 3])


with col2:
    name = st.text_input("Name")
    domicile = st.text_input("Domicile")

    cola, colb = st.columns(2)

    with cola:
        if st.button("Submit", use_container_width=True, type="primary"):
            with open(FILEPATH, "a") as f:
                f.write(f"{name.lower()},{domicile.lower()}\n")

            ph.success("Data submitted successfully!")

    with colb:
        if st.button("Delete", use_container_width=True, type="secondary"):
            ph.error("Function not Implemented yet.")


irs_data = []
with open(FILEPATH, "r") as f:
    for line in f.readlines():
        irs_data.append(line.replace("\n", "").split(","))

if irs_data:
    st.header("IRS Data")
    st.table(irs_data)
