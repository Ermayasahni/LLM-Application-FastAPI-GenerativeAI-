# pip install sqlalchemy
import streamlit as st
import requests
import mysql.connector as mysql

conn = mysql.connect(
    host = "localhost",
    user = "root",
    password = "maya1724",
    database = "LLM"
)

cursor = conn.cursor()

API_URL = "http://127.0.0.1:8000/chat"

API_URL2 = "http://127.0.0.1:8000/predict"

user_input = st.text_input("Ask something.....")

if st.button("click"):
    response = requests.post(API_URL, json = {"message" : user_input}).json()
    cursor.execute(f"""INSERT INTO response (user_input, bot_response) values (%s, %s)""", (user_input, response["result"]))
    conn.commit()
    st.write(response["result"])

user_input2 = st.number_input("Ask something for predition.....")

if st.button("Predict"):
    response = requests.post(API_URL2, json = {"year" : user_input2}).json()
    st.write(response["salary"])        