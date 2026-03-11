# AI Chatbot & Salary Prediction Web App (GenerativeAI)
 
## 📌 Project Overview
Full-stack Generative AI project using FastAPI for backend APIs, Streamlit for frontend UI, and MySQL for storing chat responses and predictions

This project is a **Generative AI application** built using **FastAPI**, **Streamlit**, and **MySQL**.
It allows users to interact with an AI chatbot, store conversation responses in a database, and perform predictions through API endpoints.

The project also demonstrates **Prompt Engineering techniques** to structure user queries and generate better AI responses.

---

## 🚀 Features

* AI Chat API
* Prompt Engineering for structured AI responses
* FastAPI Backend for API services
* MySQL Database Integration
* Streamlit Interactive UI
* Salary Prediction API

## 🛠 Tech Stack

* Python
* FastAPI
* Streamlit
* MySQL
* Requests
* Uvicorn

---

---

## 🧠 Prompt Engineering

Prompt Engineering is used to improve the quality and relevance of AI responses.

Example prompt structure:

```id="v7y9ct"
You are a helpful AI assistant.
Answer the user's question clearly and concisely.

User Question:
{user_input}

Response:
```

Benefits of Prompt Engineering in this project:

* Improves response accuracy
* Guides AI behavior
* Makes responses more structured
* Helps control tone and style of output

---


## 📂 Project Structure

```id="f3hcsf"
LLM-Applications
│
├── Backend
│   └── main.py          # FastAPI backend APIs
│
├── frontend
│   └── app.py           # Streamlit UI
│
├── requirements.txt
├── README.md
└── .gitignore
```

---


### Create Virtual Environment

```bash id="hb7s9s"
python -m venv env
```

Activate environment:

Windows

```bash id="x1rz21"
env\Scripts\activate
```

Linux / Mac

```bash id="s8xgbr"
source env/bin/activate
```

---

### Install Dependencies

```bash id="v1u31c"
pip install -r requirements.txt
```

---

## 🗄 Database Setup

Create a MySQL database:

```id="5og5xf"
Database name: LLM
```

Create table:

```sql id="or1r8s"
CREATE TABLE response (
id INT AUTO_INCREMENT PRIMARY KEY,
user_input TEXT,
bot_response TEXT
);
```

---

## ▶️ Run the Application

### Start FastAPI Backend

```bash id="6rcpfs"
uvicorn Backend.main:app --reload
```

Backend runs at:

```id="u7teqq"
http://127.0.0.1:8000
```

---

### Start Streamlit Frontend

```bash id="6jeo41"
streamlit run frontend/app.py
```

---

## 🔗 API Endpoints

### Chat API

```id="sbqavj"
POST /chat
```

Example Request:

```json id="nghsn0"
{
 "message": "What is Artificial Intelligence?"
}
```

---

### Prediction API

```id="u9y9pg"
POST /predict
```

Example Request:

```json id="y5h8ct"
{
 "year": 5
}
```

---

## 📊 Future Improvements

* Add advanced prompt engineering
* Integrate external LLM APIs
* Add authentication
* Deploy using Docker
* Cloud deployment (AWS / Azure)

---



⭐ If you like this project, consider giving it a star on GitHub!
