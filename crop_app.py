import pickle
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Home_1.html')

@app.route('/Predict')
def prediction():
    return render_template('Index.html')
@app.route('/form', methods=['POST'])
def predict():
    Nitrogen=int(request.form['Nitrogen'])
    Phosphorus=int(request.form['Phosphorus'])
    Potassium=int(request.form['Potassium'])
    Temperature=float(request.form['Temperature'])
    Humidity=float(request.form['Humidity'])
    Ph=float(request.form['ph'])
    Rainfall=float(request.form['Rainfall'])

    values=[Nitrogen,Phosphorus,Potassium,Temperature,Humidity,Ph,Rainfall]
    app = pickle.load(open("./Pickle_RL_Model.pkl", "rb"))
    print("Data Loaded successfully")
    if Ph>0 and Ph<=14 and Temperature<100 and Humidity>0:
        arr = [values]
        acc = app.predict(arr)
        # print(acc)
        return render_template('prediction.html', prediction=str(acc))
    else:
        return "Sorry...  Error in entered values in the form Please check the values and fill it again"

if __name__ == '__main__':
    app.run(debug=True)









