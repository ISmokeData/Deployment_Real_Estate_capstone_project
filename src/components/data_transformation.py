import sys, os
from os.path import dirname, join, abspath
sys.path.insert(0,abspath(join(dirname(__file__),'..')))
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler, OrdinalEncoder

from exception import CustomException
from logger import logging
from utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts','preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformation_object(self):
        try:
            logging.info('Data Transformation initiated')
            categorical_cols = ['BHK','sector','floor','Furnishing','facing','Car_Parking','Bathroom','Balcony','overlooking','city']
            numerical_cols = ['SuperArea']

            bhk_cat = ['1', '2', '3', '4', '4+']
            floor_cat = ['0','1','2','3','4','5','6','7','8','9','10','10+']
            furnishing_cat = ['Unfurnished', 'Semi-Furnished', 'Furnished']
            facing_cat = ['East','North - East','North','West','North - West','South','South - East','South -West']
            
            # Removed duplicates from the sector_cat list
            sector_cat = list(set([
                'Panathur','Thanisandra','Whitefield','others','Sarjapur Road','Sarjapura','Thanisandra Main Road','Gunjur','Chandapura','Bagaluru','Yelahanka','Outer Ring Road','Krishnarajapura','Jakkur','JP Nagar','Hennur Main Road','Hebbal','Jayanagar','HSR Layout','Kengeri',
                'Banaswadi', 'Padur','Medavakkam','Thoraipakkam','Kolathur','Perambur','Sholinganallur','Thiruvanmiyur','Perumbakkam','Manapakkam','Pallikaranai','Kilpauk','Madipakkam','Kelambakkam','Porur','Mogappair','Avadi','Velachery','Anna Nagar','Chromepet','Urapakkam','Guduvancheri',
                'Ambattur','Sector 71','Sector 111','Sector 61','Sector 63A','Sector 65','Sector 49','Sector 63','Sector 89','Sector 37D','Sector 59','Sector 113','Sector 106','Sector 51','Sector 2','Sector 26','Sector 25','Sector 102','Sector 92','Sector 57','Sector 43','Sector 79','Sector 14','Sector 24','Sector 85','Sector 36','Puppalguda','Narsingi','Kokapet','Kompally','Kondapur','Miyapur','Tellapur','Kollur','Nizampet','NH 9','Bandlaguda Jagir','Chanda Nagar','Bachupally','Yapral','Gachibowli','Outer Ring Road','Manikonda Jagir','Pragathi Nagar','Banjara Hills',
                'Uppal','Kandivali','Bhandup','Chembur','Mulund','Bandra','Borivali','Powai','Mira Road','Andheri','Malad','Goregaon','Ghatkopar','Santacruz','Worli','Virar','Prabhadevi','Kanjurmarg',
                'Vile Parle','Wadala'
            ]))
            car_parking_cat = ['available', 'not sure']
            bathroom_cat = ['1', '2', '3', '4', '4+']
            balcony_cat = ['1', '2', '3', '4', '4+']
            overlooking_cat = ['Garden/Park','Garden/Park, Pool','Garden/Park, Main Road','Garden/Park, Main Road, Pool','Main Road, Pool','Pool','Main Road']
            city_cat = ['Bangalore', 'chennai', 'Gurgaon', 'Hydrabad', 'Mumbai']

            logging.info('Pipeline Initiated')

            # Numerical Pipeline
            num_pipeline = Pipeline(
                steps=[
                    ('scaler', StandardScaler())
                ]
            )

            # Categorical Pipeline
            cat_pipeline = Pipeline(
                steps=[
                    ('ordinalencoder', OrdinalEncoder(categories=[bhk_cat, sector_cat, floor_cat, furnishing_cat,
                                                                  facing_cat, car_parking_cat, bathroom_cat, balcony_cat,
                                                                  overlooking_cat, city_cat])),
                    ('scaler', StandardScaler())
                ]
            )

            preprocessor = ColumnTransformer([
                ('num_pipeline', num_pipeline, numerical_cols),
                ('cat_pipeline', cat_pipeline, categorical_cols)
            ])

            return preprocessor

            logging.info('Pipeline Completed')

        except Exception as e:
            logging.info("Error in Data Transformation")
            raise CustomException(e, sys)

        
    
    def initaite_data_transformation(self,train_path,test_path):
        try:
            # Reading train and test data
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info('Read train and test data completed')
            logging.info(f'Train Dataframe Head : \n{train_df.head().to_string()}')
            logging.info(f'Test Dataframe Head  : \n{test_df.head().to_string()}')

            logging.info('Obtaining preprocessing object')

            preprocessing_obj = self.get_data_transformation_object()

            logging.info("removing column")
            target_column_name = 'price'
            drop_columns = [target_column_name]

            logging.info("Creating input and target data")
            input_feature_train_df = train_df.drop(columns=drop_columns,axis=1)
            target_feature_train_df=train_df[target_column_name]

            input_feature_test_df=test_df.drop(columns=drop_columns,axis=1)
            target_feature_test_df=test_df[target_column_name]
            
            logging.info("Transforming data")
            ## Trnasformating using preprocessor obj
            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)

            logging.info("Applying preprocessing object on training and testing datasets.")
            # -----
            print(input_feature_train_arr.shape)
            print(target_feature_train_df.shape)

            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            save_object(

                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj

            )
            logging.info('Preprocessor pickle file saved')

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )
            
        except Exception as e:
            logging.info("Exception occured in the initiate_datatransformation")

            raise CustomException(e,sys)
            

