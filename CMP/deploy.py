from flask import Flask, render_template, request, redirect, url_for
import pickle

app = Flask(__name__, template_folder="templat")

# Load the model
model = pickle.load(open('random_forest_model.pkl', 'rb'))

def calculate_bmi(weight, height):
    # Calculate BMI using the formula: BMI = kg/m^2
    bmi = (weight / (height ** 2))
    return bmi

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve form data
    gender = float(request.form['gender'])
    age = float(request.form['age'])
    occupation = float(request.form['occupation'])
    sleep_duration = float(request.form['sleep_duration'])
    quality_of_sleep = float(request.form['quality_of_sleep'])
    physical = float(request.form['physical'])
    stress = float(request.form['stress'])
    weight = float(request.form['weight'])
    height = float(request.form['height'])
    blood = float(request.form['blood'])
    heart = float(request.form['heart'])
    daily = float(request.form['daily']) 

    # Calculate BMI
    bmi = calculate_bmi(weight, height)

    # Predict using the model
    result = model.predict([[gender, age, occupation, sleep_duration, quality_of_sleep, physical, stress, bmi, blood, heart, daily]])[0]

    # Redirect to result page with the result as a query parameter
    return redirect(url_for('result', result=result))

@app.route('/result')
def result():
    # Get the result from the query parameter
    result = request.args.get('result')
    return render_template('result.html', result=result)

# Define route for index.html
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/reso.html')
def reso():
    return render_template('reso.html')

@app.route('/alarm.html')
def alarm():
    return render_template('alarm.html')

if __name__ == '__main__':
    app.run(debug=True,port=5001)