import streamlit as st
from src.pipelines.prediction_pipeline import CustomData,PredictPipeline
from src.pipelines.training_pipeline import TrainingPipeline

st.set_page_config(page_title="Price Prediction", page_icon="🤖", layout="wide")

# property_type

st.header("Price Prediction")

city = st.selectbox("**Select City**",['Bangalore', 'chennai', 'Gurgaon', 'Hydrabad', 'Mumbai'])

BHK = st.selectbox("**Select BHK**", ['1', '2', '3', '4', '4+'])

if city == 'Bangalore':
    sector = st.selectbox("**select Area**",['Panathur',
        'Thanisandra',
        'Whitefield',
        'others',
        'Sarjapur Road',
        'Sarjapura',
        'Thanisandra Main Road',
        'Gunjur',
        'Chandapura',
        'Bagaluru',
        'Yelahanka',
        'Outer Ring Road',
        'Krishnarajapura',
        'Jakkur',
        'JP Nagar',
        'Hennur Main Road',
        'Hebbal',
        'Jayanagar',
        'HSR Layout',
        'Kengeri',
        'Banaswadi'])
elif city == 'chennai':
    sector = st.selectbox("**select Area**",['others',
 'Padur',
 'Medavakkam',
 'Thoraipakkam',
 'Kolathur',
 'Perambur',
 'Sholinganallur',
 'Thiruvanmiyur',
 'Perumbakkam',
 'Manapakkam',
 'Pallikaranai',
 'Kilpauk',
 'Madipakkam',
 'Kelambakkam',
 'Porur',
 'Mogappair',
 'Avadi',
 'Velachery',
 'Anna Nagar',
 'Chromepet',
 'Urapakkam',
 'Guduvancheri',
 'Ambattur']
)    
elif city == 'Gurgaon':
    sector = st.selectbox("**select Area**",['Sector 71',
 'others',
 'Sector 111',
 'Sector 61',
 'Sector 63A',
 'Sector 65',
 'Sector 49',
 'Sector 63',
 'Sector 89',
 'Sector 37D',
 'Sector 59',
 'Sector 113',
 'Sector 106',
 'Sector 51',
 'Sector 2',
 'Sector 26',
 'Sector 25',
 'Sector 102',
 'Sector 92',
 'Sector 57',
 'Sector 43',
 'Sector 79',
 'Sector 14',
 'Sector 24',
 'Sector 85',
 'Sector 36'])
    
elif city == 'Hydrabad':
    sector = st.selectbox("**select Area**",['Puppalguda',
 'Narsingi',
 'Kokapet',
 'Kompally',
 'Kondapur',
 'Miyapur',
 'Tellapur',
 'Kollur',
 'others',
 'Nizampet',
 'NH 9',
 'Bandlaguda Jagir',
 'Chanda Nagar',
 'Bachupally',
 'Yapral',
 'Gachibowli',
 'Outer Ring Road',
 'Manikonda Jagir',
 'Pragathi Nagar',
 'Banjara Hills',
 'Uppal'])
    
elif city == 'Mumbai':
    sector = st.selectbox("**select Area**",['Wadala',
 'others',
 'Kandivali',
 'Bhandup',
 'Chembur',
 'Mulund',
 'Bandra',
 'Borivali',
 'Powai',
 'Mira Road',
 'Andheri',
 'Malad',
 'Goregaon',
 'Ghatkopar',
 'Santacruz',
 'Worli',
 'Virar',
 'Prabhadevi',
 'Kanjurmarg',
 'Vile Parle'])

SuperArea = st.number_input("**Super Area in Sqft**", min_value=0, max_value=10000, value=0)
SuperArea = float(SuperArea)

floor = st.selectbox("**Floor**",['0','1','2','3','4','5','6','7','8','9','10','10+'])

Furnishing = st.selectbox("**Furnishing**",['Unfurnished', 'Semi-Furnished', 'Furnished'])

facing = st.selectbox("**Facing**",['East',
 'North - East',
 'North',
 'West',
 'North - West',
 'South',
 'South - East',
 'South -West'])

car_parking = st.selectbox("**Car Parking**",['available', 'not sure'])

bathroom = st.selectbox("**Bathroom**",['1', '2', '3', '4', '4+'])

balcony = st.selectbox("**Balcony**",['1', '2', '3', '4', '4+'])

overlooking = st.selectbox("**Overlooking**",['Garden/Park',
 'Garden/Park, Pool',
 'Garden/Park, Main Road',
 'Garden/Park, Main Road, Pool',
 'Main Road, Pool',
 'Pool',
 'Main Road'])
if st.button("Predict Price"):
    train = TrainingPipeline()
    train.train()
    data = CustomData(BHK, sector, SuperArea, floor, Furnishing, facing, car_parking, bathroom, balcony, overlooking, city)
    final_new_data = data.get_data_as_datarframe()
    predict_Pipeline = PredictPipeline()
    pred = predict_Pipeline.predict(final_new_data)
    st.write(pred)






# <--------------------------------------------------------------------------->
background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://sugamhomes.com/assets/images/Hunger/AERIAL_VIEW_03_NIGHT_HIRES.webp");
    background-size: 100vw 100vh;  # This sets the size to cover 100% of the viewport width and height
    background-position: center;  
    background-repeat: no-repeat;
}
</style>
"""

st.markdown(background_image, unsafe_allow_html=True)

# st.text_input("", placeholder="Streamlit CSS ")

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
