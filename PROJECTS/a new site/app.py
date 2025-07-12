from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/project', methods=['GET', 'POST'])
def predict():
    prediction = None  # Initialize variable

    if request.method == 'POST':
        brand = request.form['brand_name']
        model_name = request.form['bike_model']
        cc = int(request.form['cc'])
        year = int(request.form['year'])
        kms = int(request.form['kms_driven'])

        # Dummy price prediction logic
        prediction = round(30000 + (cc * 5) - (kms * 0.5) + ((2025 - year) * -1000), 2)

    return render_template('project.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)


