# import streamlit as st
# import pickle
# import numpy as np
#
# # Load the model
# try:
#     model = pickle.load(open('C:\Users\snehal devkar\PycharmProjects\PythonProject1\regmodel (1).pkl', 'rb'))
# except FileNotFoundError:
#     st.error("Model file 'regmodel (1).pkl' not found. Please check the file path.")
#     st.stop()
#
#
# # Streamlit app
# st.title("Real Estate Price Prediction")
# st.write("Enter the property details below to get the predicted price.")
#
# # Collect user inputs
# square_feet = st.number_input("Square Feet", min_value=100, max_value=10000, step=10)
# num_bedrooms = st.number_input("Number of Bedrooms", min_value=0, max_value=20, step=1)
# num_bathrooms = st.number_input("Number of Bathrooms", min_value=0, max_value=20, step=1)
# num_floors = st.number_input("Number of Floors", min_value=1, max_value=5, step=1)
# year_built = st.number_input("Year Built", min_value=1800, max_value=2025, step=1)
# has_garden = st.selectbox("Has Garden?", [0, 1])  # 0: No, 1: Yes
# has_pool = st.selectbox("Has Pool?", [0, 1])  # 0: No, 1: Yes
# garage_size = st.number_input("Garage Size (Number of Cars)", min_value=0, max_value=10, step=1)
# location_score = st.slider("Location Score (1-100)", min_value=1, max_value=100)
# distance_to_center = st.number_input("Distance to City Center (km)", min_value=0.0, step=0.1)
#
# # Predict button
# if st.button("Predict"):
#     # Prepare input data
#     input_data = np.array([[square_feet, num_bedrooms, num_bathrooms, num_floors, year_built,
#                             has_garden, has_pool, garage_size, location_score, distance_to_center]])
#
#     # # Scale the input data if scaler is used
#     # input_scaled = scaler.transform(input_data)
#     #
#     # # Make prediction
#     prediction = model.predict(input_data)
#
#     # Display the result
#     st.success(f"The predicted house price is: ${prediction[0]:,.2f}")
#
#












import streamlit as st
import pickle
import numpy as np
import os

# 🔹 Set the absolute path to the model file
MODEL_PATH = r"C:\Users\snehal devkar\PycharmProjects\PythonProject1\regmodel (1).pkl"

# 🔹 Load the model
try:
    with open(MODEL_PATH, "rb") as file:
        model = pickle.load(file)
except FileNotFoundError:
    st.error(f"🚨 Model file not found at: {MODEL_PATH}. Please check the file path.")
    st.stop()
except Exception as e:
    st.error(f"🚨 Error loading model: {e}")
    st.stop()

# 🔹 Streamlit app interface
st.title("🏡 Real Estate Price Prediction")
st.write("Enter the property details below to get the predicted price.")

# 🔹 Collect user inputs
square_feet = st.number_input("📏 Square Feet", min_value=100, max_value=10000, step=10)
num_bedrooms = st.number_input("🛏 Number of Bedrooms", min_value=0, max_value=20, step=1)
num_bathrooms = st.number_input("🛁 Number of Bathrooms", min_value=0, max_value=20, step=1)
num_floors = st.number_input("🏢 Number of Floors", min_value=1, max_value=5, step=1)
year_built = st.number_input("📅 Year Built", min_value=1800, max_value=2025, step=1)
has_garden = st.selectbox("🌳 Has Garden?", [0, 1])  # 0: No, 1: Yes
has_pool = st.selectbox("🏊 Has Pool?", [0, 1])  # 0: No, 1: Yes
garage_size = st.number_input("🚗 Garage Size (Number of Cars)", min_value=0, max_value=10, step=1)
location_score = st.slider("📍 Location Score (1-100)", min_value=1, max_value=100)
distance_to_center = st.number_input("📍 Distance to City Center (km)", min_value=0.0, step=0.1)

# 🔹 Predict button
if st.button("🔮 Predict Price"):
    try:
        # Prepare input data
        input_data = np.array([[square_feet, num_bedrooms, num_bathrooms, num_floors, year_built,
                                has_garden, has_pool, garage_size, location_score, distance_to_center]])

        # Make prediction
        prediction = model.predict(input_data)

        # Display the result
        st.success(f"💰 The predicted house price is: **${prediction[0]:,.2f}**")

    except Exception as e:
        st.error(f"🚨 Prediction Error: {e}")

