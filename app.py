from flask import Flask,request,render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline 

application=Flask(__name__) ##initilaize the flask

app=application

## Route for a home page

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html') ## simple input data field that we need to provide to model 
    else:
        data=CustomData(
            gender=request.form.get('gender'), ## reading all the values from the form
            race_ethnicity=request.form.get('ethnicity'),## we will get the ethnicity information
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('writing_score')),
            writing_score=float(request.form.get('reading_score')))
        
        pred_df=data.get_data_as_data_frame() ## present under custom data
        print(pred_df)

        predict_pipeline=PredictPipeline()
        results=predict_pipeline.predict(pred_df) ## call predict fnx then put pred_df inside it 
        return render_template('home.html',results=results[0]) ## 0 becz it is in the list format and all the value will return
    ##	•	render_template('home.html', results=results[0]) means:
    #“Show the home.html page and pass the first item of results to it.”
	#•	If results = ["Apple", "Banana", "Cherry"], then results[0] is "Apple".
    

if __name__=="__main__":      
    app.run(debug=True,host="0.0.0.0",port=80) ## Open your browser and go to: ##http://127.0.0.1/ and http://127.0.0.1/predictdata      


