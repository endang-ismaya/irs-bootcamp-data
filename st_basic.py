import streamlit as st

st.title("Rogers Migration App")
st.divider()

st.header("2G Migrations")

st.code(
    """
print("Hello Streamlit")

def add(num1: int, num2: int) -> int:
    return num1 + num2
)
""",
    language="python",
)

st.write(
    "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
)

dt_irs = {"Rogers": ["Alfian", "Guan", "Faisal", "Fikky"], "Voda": ["Wisnu", "Arsi"]}

st.write(dt_irs)

st.markdown("*Streamlit* is **really** ***cool***.")
st.markdown("""
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.""")
st.markdown(
    "Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:"
)

multi = """If you end a line with two spaces,
a soft return is used for the next line.

Two (or more) newline characters in a row will result in a hard return.
"""
st.markdown(multi)

st.markdown(":material/home:")
st.markdown(":material/close:")
