# House Price Prediction

This project aims to predict house prices based on various input features such as the number of bedrooms, bathrooms, square footage, condition, and year of construction. By leveraging machine learning algorithms, the model provides real-time predictions to estimate house prices, making it a valuable tool for homeowners, real estate agents, and developers.

## Technologies Used

- **Python**: The programming language used for data analysis, model training, and building the web application.
- **Scikit-learn**: A machine learning library used to build and evaluate the predictive model.
- **Flask**: A lightweight web framework used for building the back-end API and web interface.
- **Tailwind CSS**: A utility-first CSS framework used to style the front-end for a responsive, modern design.
- **Git**: Version control used for tracking code changes and collaboration.
- **GitHub**: For hosting the project and providing a platform for collaboration.

## Project Overview

1. **Data Preprocessing**:
   - The dataset consists of features like `bedrooms`, `bathrooms`, `sqft_living`, `sqft_lot`, and more.
   - The target variable, `price`, is excluded from the standardization process as it’s the value to be predicted.
   - The data is cleaned, missing values are handled, and numerical features are standardized for better model performance.

2. **Model Building**:
   - A machine learning model (such as **Linear Regression** or **Random Forest**) is trained using the cleaned data to predict the `price` of a house.
   - The model's performance is evaluated using metrics like Mean Absolute Error (MAE), Mean Squared Error (MSE), and R-squared to assess the accuracy of predictions.

3. **Web Application with Flask**:
   - The trained model is integrated into a Flask web application to allow real-time predictions via a user-friendly interface.
   - Users can input house features (like the number of bedrooms, bathrooms, etc.) and receive an estimated price for the house.

4. **Dynamic Front-End**:
   - Tailwind CSS ensures that the front-end is responsive and visually appealing across various devices and screen sizes.
   - The form input is dynamically handled, allowing for seamless interaction between the user and the model.

5. **Version Control and Deployment**:
   - The project is version-controlled using **Git** and is hosted on **GitHub** for easy collaboration and tracking of changes.

## Features

- **Real-time House Price Prediction**: Users can enter house details and instantly get a price estimate.
- **Responsive Design**: The application is fully responsive, ensuring a good user experience across desktop and mobile devices.
- **Interactive Form**: Users can fill in house features, such as the number of bedrooms, bathrooms, square footage, etc., and get a price prediction.
- **Model Accuracy**: The machine learning model is evaluated using various metrics, ensuring that it provides reliable price predictions.

## Installation

To get started with the project, follow these steps:

### Prerequisites

Ensure you have Python installed on your machine.

### Steps

1. Clone the repository:
```bash
   git clone https://github.com/sameeksharshetty24/House-Price-Prediction.git
```
2.Navigate to the project directory:
```bash
  cd House-Price-Prediction
```
3.Create a virtual environment (optional but recommended):
```bash
  python -m venv venv
```
4.Activate the virtual environment:
**Windows:**
```bash
venv\Scripts\activate
```
***macOS/Linux:***
```bash
source venv/bin/activate
```
5.Install the required dependencies:

bash
pip install -r requirements.txt
6.Run the Flask application:
```bash
python app.py
```
7.Open your browser and go to http://localhost:5000 to use the web application.
