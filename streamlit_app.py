#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pickle
import os
import numpy as np
import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import datetime

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Bank Customer Churn Prediction", layout="centered")

# ---------------- LOAD MODEL ----------------
# Set path to models
model = pickle.load(open("bank_customer_chrun.sav", 'rb'))

# ---------------- VISITOR COUNTER ----------------
counter_file = "visitor_data.pkl"

if os.path.exists(counter_file):
    with open(counter_file, 'rb') as f:
        visitor_data = pickle.load(f)
else:
    visitor_data = {'count': 0, 'timestamps': []}

if 'counted' not in st.session_state:
    st.session_state['counted'] = True
    visitor_data['count'] += 1
    visitor_data['timestamps'].append(str(datetime.datetime.now()))
    with open(counter_file, 'wb') as f:
        pickle.dump(visitor_data, f)

# ---------------- SIDEBAR MENU ----------------
with st.sidebar:
    selected = option_menu("Main Menu", 
                           ["Welcome", "Prediction", "FAQ", "Disclaimer", "Analytics", "Donate & Support"], 
                           icons=['house', 'activity', 'question-circle', 'exclamation-circle', 'bar-chart'],
                           menu_icon="cast", default_index=0)

# ---------------- WELCOME PAGE ----------------
if selected == "Welcome":
    st.markdown("<h1 style='text-align: center; color: green;'>🏦 Bank Customer Churn Prediction</h1>", unsafe_allow_html=True)
    st.success(f"👥 *Total Visitors:* {visitor_data['count']}")
    st.write("""
    Predict whether a bank customer is likely to leave using this intelligent machine learning tool.

    ✅ Easy input form  
    ✅ Accurate churn predictions  
    ✅ Business insights for customer retention

    👉 Use the sidebar to begin prediction!
    """)

# ---------------- PREDICTION PAGE ----------------
elif selected == "Prediction":
    st.markdown("<h2 style='text-align: center;'>🔍 Predict Customer Churn</h2>", unsafe_allow_html=True)
    st.write("Fill in the customer's details:")

    with st.form("churn_form"):
        credit_score = st.number_input("Credit Score", 300, 900)
        age = st.number_input("Age", 18, 100)
        tenure = st.number_input("Years with Bank", 0, 20)
        balance = st.number_input("Account Balance", 0.0, 250000.0)
        num_of_products = st.selectbox("Number of Products", [1, 2, 3, 4])
        has_cr_card = st.selectbox("Has Credit Card?", ["Yes", "No"])
        is_active = st.selectbox("Is Active Member?", ["Yes", "No"])
        estimated_salary = st.number_input("Estimated Salary", 0.0, 200000.0)
        geography = st.selectbox("Geography", ["France", "Spain", "Germany"])
        gender = st.selectbox("Gender", ["Male", "Female"])
        submit = st.form_submit_button("Predict Churn")

    if submit:
        # Encoding
        gender_val = 1 if gender == "Male" else 0
        geography_val = {"France": 0, "Spain": 1, "Germany": 2}[geography]
        has_cr_card_val = 1 if has_cr_card == "Yes" else 0
        is_active_val = 1 if is_active == "Yes" else 0

        # Input array for prediction
        input_data = np.array([[
            credit_score, gender_val, age, tenure, balance,
            num_of_products, has_cr_card_val, is_active_val,
            estimated_salary, geography_val
        ]])

        prediction = model.predict(input_data)[0]
        result = "Yes, the customer is likely to churn." if prediction == 1 else "No, the customer is likely to stay."
        st.success(f"📉 *Prediction:* {result}")

# ---------------- FAQ PAGE ----------------
elif selected == "FAQ":
    st.markdown("<h2 style='text-align: center;'>❓ Frequently Asked Questions</h2>", unsafe_allow_html=True)

    with st.expander("📌 What does this app do?"):
        st.write("It predicts whether a bank customer is likely to churn using machine learning.")

    with st.expander("📌 How was the model trained?"):
        st.write("The model was trained using historical customer data with features like age, balance, salary, etc.")

    with st.expander("📌 How accurate is the prediction?"):
        st.write("It depends on the model selected. Random Forest achieved 95% accuracy based on training data.")

    with st.expander("📌 Can I use this on my own data?"):
        st.write("Yes, you can adapt this app or contact the developer for a customized version.")

# ---------------- DISCLAIMER PAGE ----------------
elif selected == "Disclaimer":
    st.markdown("<h2 style='text-align: center;'>⚠ Disclaimer</h2>", unsafe_allow_html=True)
    st.warning("""
    - This app is for educational and business insight purposes only.
    - It should not be used as the sole decision-making tool for financial operations.
    - Predictions are based on historical data patterns and may vary.
    """)

# ---------------- ANALYTICS PAGE ----------------
elif selected == "Analytics":
    st.markdown("<h2 style='text-align: center;'>📊 Visitor Analytics</h2>", unsafe_allow_html=True)
    st.info(f"👥 *Total Visitors:* {visitor_data['count']}")

    if visitor_data['timestamps']:
        st.write("### 🕒 Visitor Log")
        st.dataframe(visitor_data['timestamps'])

# ---------------- DONATION PAGE ----------------
elif selected == "Donate & Support":
    st.markdown("<h2 style='text-align: center;'>💖 Support My Work</h2>", unsafe_allow_html=True)
    st.write("""
    If this tool has helped you and you'd like to support its further development, please consider donating 🙏

    - *PayPal:* dataquestsolutions2@gmail.com  
    - *Buy Me a Coffee (M-Pesa):* +254701344230  
    - *M-Pesa Paybill (Kenya):*  
        - *Paybill:* 522522  
        - *Account Number:* 1340849054  

    Every contribution supports further AI development in business and finance 💚
    """)
