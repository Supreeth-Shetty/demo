
from flask import Flask, render_template, request, url_for
import pickle
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
app = Flask(__name__)

@app.route('/profile')
def profile():
        return render_template('profile.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            Process_temperature = float(request.form['Process temperature [K]'])
            Rotational_speed = float(request.form['Rotational speed [rpm]'])
            Torque = float(request.form['Torque [Nm]'])
            Tool_wear = float(request.form['Tool wear [min]'])
            TWF = float(request.form['TWF'])
            HDF = float(request.form['HDF'])
            PWF = float(request.form['PWF'])
            OSF = float(request.form['OSF'])
            RNF = float(request.form['RNF'])

            file_name = 'ridge.pickle'
            model = pickle.load(open(file_name, 'rb'))
            prediction = model.predict(scaler.fit_transform([[Process_temperature, Rotational_speed, Torque,
                                                              Tool_wear, TWF, HDF, PWF, OSF, RNF]]))

            return render_template('results.html', prediction=round(prediction[0],2) )
        except Exception as e:
            print("Error occured", e)
    else:
        return render_template('index.html')



#def main():
# my code for profiling
    #import pandas as pd
    #import pandas_profiling
    #df = pd.read_csv('ai4i2020.csv')
    #profile = pandas_profiling.ProfileReport(df)
    #profile.to_file("profile.html")

if __name__ == "__main__":
    app.run()