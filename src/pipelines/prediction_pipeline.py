import sys, os
from os.path import dirname, join, abspath
sys.path.insert(0,abspath(join(dirname(__file__),'..')))

from exception import CustomException
from logger import logging
from utils import load_object
import pandas as pd

class PredictPipeline:
    def __init__(self):
        pass
    def predict(self,features):
        try:
            preprocessor_path = os.path.join('artifacts','preprocessor.pkl')
            model_path = os.path.join('artifacts', 'model.pkl')

            preprocessor = load_object(preprocessor_path)
            model = load_object(model_path)

            data_scaled = preprocessor.transform(features)

            pred = model.predict(data_scaled)
            return pred
        
        except Exception as e:
            logging.info('Exception occured in prediction')
            raise CustomException(e, sys)
        

class CustomData:
    def __init__(self,
                 BHK:str,
                 sector: str,
                 SuperArea:float,
                 floor:str,
                 Furnishing:str,
                 facing:str,
                 Car_Parking:str,
                 Bathroom:str,
                 Balcony:str,
                 overlooking:str,
                 city:str):
        self.BHK = BHK
        self.sector = sector
        self.SuperArea = SuperArea
        self.floor = floor
        self.Furnishing = Furnishing
        self.facing = facing
        self.Car_Parking = Car_Parking
        self.Bathroom = Bathroom
        self.Balcony = Balcony
        self.overlooking = overlooking
        self.city = city


    def get_data_as_datarframe(self):
        try:
            custom_data_input_dict = {
                'BHK':[self.BHK],
                'sector':[self.sector],
                'SuperArea':[self.SuperArea],
                'floor':[self.floor],
                'Furnishing':[self.Furnishing],
                'facing':[self.facing],
                'Car_Parking':[self.Car_Parking],
                'Bathroom':[self.Bathroom],
                'Balcony':[self.Balcony],
                'overlooking':[self.overlooking],
                'city':[self.city]
            }
            df = pd.DataFrame(custom_data_input_dict)
            logging.info('Dataframe Gathered')
            return df
        
        except Exception as e:
            logging.info('Exception occured in prediction pipeline')
            raise CustomException(e,sys)