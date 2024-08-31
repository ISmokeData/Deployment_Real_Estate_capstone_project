import streamlit as st

# Set the background image
# CSS for setting up the background with a blur effect
original_title = '<h1 style="font-family: serif; color:Brown; font-size: 40px; text-align: center; -webkit-text-stroke: 1px black;">Find your perfect home with our curated real estate listings</h1>'
st.markdown(original_title, unsafe_allow_html=True)

original_title = '<h1 style="font-family: serif; color:black; font-size: 20px; text-align: left;">Find your perfect home with our curated real estate listings</h1>'
st.markdown(original_title, unsafe_allow_html=True)

temperature = "hello"

st.write(f"temprature: :orange[{temperature}]")
background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://png.pngtree.com/background/20230527/original/pngtree-3d-model-of-an-apartment-building-picture-image_2755481.jpg");
    background-size: 100vw 100vh;  # This sets the size to cover 100% of the viewport width and height
    background-position: center;  
    background-repeat: no-repeat;

    -webkit-filter: blur(0px);
}
</style>
"""

st.markdown(background_image, unsafe_allow_html=True)
temperature = "-10"


input_style = """
<style>
input[type="text"] {
    background-color: transparent;
    color: #a19eae;  // This changes the text color inside the input box
}
div[data-baseweb="base-input"] {
    background-color: transparent !important;
}
[data-testid="stAppViewContainer"] {
    background-color: transparent !important;
}
</style>
"""