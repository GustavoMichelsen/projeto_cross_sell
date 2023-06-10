import pandas as pd
import pickle

from flask import Flask, request, Response
from cross_sell_classifier.cross_sell_classifier import CrossSell

# loading model
model = pickle.load(open('/Users/gtvmi/OneDrive/Documentos/Repos/projeto_health_insurance_cross_sell/model/dtc_cross_sell_model.plk', 'rb'))

app = Flask( __name__ )

@app.route('/cross_sell/predict', methods=['POST'])

def cross_sell():
    test_json = request.get_json()
    
    if test_json: # there is data
        if isinstance(test_json, dict): #unique example
            test_raw = pd.DataFrame(test_json, index=[0])
        else:
            test_raw = pd.DataFrame(test_json, columns=test_json[0].keys())
            
        # Instantiate CrossSell Class
        pipeline = CrossSell()
        df_raw = test_raw.copy()
        # data cleaning
        df_cleaning = pipeline.data_cleaning(df_raw)
        
        # feature engineering
        df_fe = pipeline.feature_engineering(df_cleaning)
        
        # data preparation
        df_preparation = pipeline.data_preparation(df_fe)
        
        # prediction
        df_response = pipeline.get_classifier(model, test_raw, df_preparation)
        
        return df_response
    else: 
        return Response('{}', status=200, mimetype='application/json')
    

if __name__ == "__main__":
    app.run('0.0.0.0')