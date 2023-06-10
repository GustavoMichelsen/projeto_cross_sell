import pickle
import pandas as pd
import inflection


class CrossSell(object):
    def __init__(self):
        self.home_path = '/Users/gtvmi/OneDrive/Documentos/Repos/projeto_health_insurance_cross_sell/'
        self.annual_premium_scaler = pickle.load(open(self.home_path + 'parameter/annual_premium_scaler.plk', 'rb'))
        
    def data_cleaning(self, data):
        # Columns name
        old_columns = list(data.columns)
        snekecase = lambda x: inflection.underscore(x)
        new_columns = list(map(snekecase, old_columns))
        data.columns = new_columns
        
        return data
    
    def feature_engineering(self, data):
        # Tranform gender in 1 to Male and 0 to Famale
        data['gender'] = data['gender'].apply(lambda x: 1 if x == 'Male' else 0)

        # Transform vihicle_age
        # < 1 Year = 0
        # 1-2 Year = 1
        # > 2 Years = 2
        data['vehicle_age'] = data['vehicle_age'].apply(lambda x: 0 if x == '< 1 Year' else
                                                                  1 if x == '1-2 Year' else
                                                                  2)
        # Vehicle_damege | If vihicle dameged in the past
        # 1 if Yes, 0 if No
        data['vehicle_damage'] = data['vehicle_damage'].apply(lambda x: 1 if x == 'Yes' else 0)
        
        return data
    
    def data_preparation(self, data):
        # Rescaling
        data['annual_premium'] = self.annual_premium_scaler.fit_transform(data[['annual_premium']].values)
        # Cols Drop
        cols_drop = ['id','driving_license', 'gender']
        data = data.drop(columns=cols_drop)
        return data
    
    def get_classifier(self, model, original_data, test_data):
        # Classification
        clas = model.predict_proba(test_data)
        
        # join pred into the original data
        original_data['Classification'] = clas[:, 1]
        
        return original_data.to_json(orient='records', date_format='iso')