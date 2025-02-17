from flask import Flask, render_template, request
import joblib
import numpy as np

# Load the trained model
model = joblib.load('model/house_price_model.pkl')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from the user input form
    bedrooms = float(request.form['bedrooms'])
    bathrooms = float(request.form['bathrooms'])
    sqft_living = float(request.form['sqft_living'])
    sqft_lot = float(request.form['sqft_lot'])
    floors = float(request.form['floors'])
    waterfront = float(request.form['waterfront'])
    view = float(request.form['view'])
    condition = float(request.form['condition'])
    sqft_above = float(request.form['sqft_above'])
    sqft_basement = float(request.form['sqft_basement'])
    yr_built = float(request.form['yr_built'])
    yr_renovated = float(request.form['yr_renovated'])

    # Create a numpy array of the features
    input_data = np.array([[bedrooms, bathrooms, sqft_living, sqft_lot, floors, 
                            waterfront, view, condition, sqft_above, sqft_basement, 
                            yr_built, yr_renovated]])

    # Make predictions using the trained model
    predicted_price = model.predict(input_data)

    # Return the prediction result
    return render_template('index.html', prediction_text=f'Predicted House Price: {predicted_price[0]:,.2f}')

if __name__ == "__main__":
    app.run(debug=True)
