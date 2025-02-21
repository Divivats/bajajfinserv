# 🚀 Bajaj Finserv API

An API built using **FastAPI** for processing input data by categorizing numbers and alphabets while identifying the highest alphabet. This API is deployed on **Render** and ready for integration with a frontend.

## 🌍 Live API URL

🔗 **Base URL:** [https://bajajfinserv-08kk.onrender.com](https://bajajfinserv-08kk.onrender.com)

---

## 📌 Features

✅ Categorizes input into numbers and alphabets\
✅ Identifies the highest alphabet\
✅ Provides an operation code via a GET request\
✅ CORS enabled for seamless frontend integration\
✅ Deployed and accessible online

---

## 🛠 Installation & Setup

### **1️⃣ Clone the Repository**

```sh
$ git clone https://github.com/Divivats/bajajfinserv.git
$ cd bajajfinserv
```

### **2️⃣ Create a Virtual Environment** (Optional but recommended)

```sh
$ python -m venv venv
$ source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### **3️⃣ Install Dependencies**

```sh
$ pip install -r requirements.txt
```

### **4️⃣ Run the Server Locally**

```sh
$ uvicorn main:app --host 0.0.0.0 --port 10000
```

🚀 API will now be running at: [**http://localhost:10000**](http://localhost:10000)

---

## 📡 API Endpoints

### 🔹 **1. Process Data** (POST)

- **Endpoint:** `/bfhl`
- **Method:** `POST`
- **Request Body (JSON):**

```json
{
  "data": ["A", "B", "C", "1", "2", "3"]
}
```

- **Response:**

```json
{
  "is_success": true,
  "user_id": "divyansh_vats_22BAI71419",
  "email": "your-email@example.com",
  "roll_number": "22AML4A",
  "numbers": ["1", "2", "3"],
  "alphabets": ["A", "B", "C"],
  "highest_alphabet": ["C"]
}
```

### 🔹 **2. Get Operation Code** (GET)

- **Endpoint:** `/bfhl`
- **Method:** `GET`
- **Response:**

```json
{
  "operation_code": 1
}
```

---

## 🌐 Deployment on Render

This API is hosted on **Render**. If deploying manually, ensure:

1. The `requirements.txt` includes all dependencies.
2. The `main.py` file runs with `uvicorn`.
3. CORS middleware is added for frontend integration.

---

## 🚀 Frontend Integration

🔗 **Frontend URL:** [https://resonant-cocada-5761dc.netlify.app](https://resonant-cocada-5761dc.netlify.app)

To connect the frontend with this API:

- Ensure API calls are made to `https://bajajfinserv-08kk.onrender.com/bfhl`
- Use Fetch or Axios in JavaScript:

```js
fetch("https://bajajfinserv-08kk.onrender.com/bfhl", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ data: ["A", "B", "C", "1", "2", "3"] })
})
.then(response => response.json())
.then(data => console.log(data));
```

---

## 📝 License

This project is open-source and available for modification and improvement.

🚀 **Developed by Divyansh Vats (22BAI71419) | Bajaj Finserv Intern-Test** 🚀

