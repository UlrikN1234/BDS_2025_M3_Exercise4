# 🚀 Business Plan Generator  

A FastAPI and Streamlit-based application that uses AI agents to generate a **business plan** based on user inputs.  

## 📌 Project Overview  

This project consists of:  

1. **FastAPI Backend (`app.py`)**  
   - Handles requests from the frontend.  
   - Uses multiple AI-powered agents to generate a business plan.  
   - Returns the generated output to the frontend.  

2. **Streamlit Frontend (`streamlit_app.py`)**  
   - Provides a simple interface for users to input business details.  
   - Sends user inputs to the backend via API calls.  
   - Displays the generated business plan.  

---

## 📂 Project Structure  

```
📁 Business-Plan-Generator  
│── app.py  # FastAPI backend  
│── streamlit_app.py  # Streamlit frontend  
│── agents.py  # AI Agents definitions  
│── tasks.py  # AI Tasks definitions  
│── requirements.txt  # Dependencies  
│── README.md  # Project documentation  
```

---

## 🛠 Installation  

### 1️⃣ Clone the Repository  
```sh
git clone https://github.com/UlrikN1234/BDS_2025_M3_Exercise3-.git  
cd BDS_2025_M3_Exercise3- 
```

### 2️⃣ Create a Virtual Environment (Optional but Recommended)  
```sh
python -m venv venv  
source venv/bin/activate  # macOS/Linux  
venv\Scripts\activate  # Windows  
```

### 3️⃣ Install Dependencies  
```sh
pip install -r requirements.txt  
```

---

## 🚀 Running the Application  

### 1️⃣ Start the Backend (FastAPI)  
```sh
uvicorn app:app --host 127.0.0.1 --port 8000 --reload  
```

> The API should now be running at `http://127.0.0.1:8000/`  
> You can check the API docs at `http://127.0.0.1:8000/docs`

### 2️⃣ Start the Frontend (Streamlit)  
```sh
streamlit run streamlit_app.py  
```

> The Streamlit app should open in your browser.  

---

## 📡 API Endpoints  

| Method | Endpoint | Description |  
|--------|------------|-------------|  
| **POST** | `/run_agents` | Runs AI agents to generate a business plan |  
| **GET** | `/` | Health check endpoint |  

---

## 🖥 Usage  

1. Open the Streamlit app in your browser.  
2. Enter your **Business Name, Business Idea, and Vision**.  
3. Click the **"Run Business Plan Generator"** button.  
4. Wait for AI agents to process the request.  
5. View the **generated business plan** in the text area.  

---

## 🔧 Deployment  

### Deploying FastAPI Backend  

You can deploy the FastAPI backend using:  

- **Docker**  
- **Cloud platforms** like **AWS, GCP, or Azure**  
- **Hosting services** like **Railway, Render, or Hugging Face Spaces**  

### Deploying Streamlit Frontend  

For deploying Streamlit, you can use:  

- **Streamlit Cloud**  
- **Hugging Face Spaces**  
- **Heroku**  

---

## ⚙️ Nodes 

System Requirements:
Python Version: 3.12 or lower (Python 3.9+ recommended for compatibility with dependencies)

## 🤝 Contributions  

Feel free to open an **issue** or submit a **pull request**!  

---

## 📜 License  

This project is licensed under the **MIT License**.  
