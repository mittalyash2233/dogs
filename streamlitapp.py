import streamlit as st

st.title("🐶 Happy Paws")

st.write("Welcome to Happy Paws Dog Seller!")

breed = st.selectbox(
    "Choose a dog breed",
    ["Golden Retriever", "Beagle", "German Shepherd"]
)

if st.button("Buy Now"):
    st.success(f"Thank you for choosing the {breed}! We'll contact you soon.")
