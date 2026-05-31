# Customer Churn Prediction 📊

## 📌 Project Overview

This project focuses on predicting customer churn using machine learning techniques. The goal is to identify customers who are likely to leave a telecom service based on their usage patterns and service details. This helps businesses take proactive actions to retain customers.

The model is built using **Logistic Regression** and trained on a real-world telecom dataset.

---

## 📂 Dataset Information

* Source: Telecom customer churn dataset
* Total Records: 7043 customers
* Features: 20 input features + 1 target variable (Churn)
* Target:

  * `0` → No Churn
  * `1` → Churn

---

## 🛠️ Technologies Used

* Python 🐍
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Jupyter Notebook

---

## 🔍 Data Preprocessing Steps

* Handled missing values in `TotalCharges`
* Converted categorical variables using **One-Hot Encoding**
* Dropped irrelevant column: `customerID`
* Converted target variable `Churn` into binary format
* Split dataset into training and testing sets

---

## 🤖 Model Building

* Algorithm used: Logistic Regression
* Train-test split: 80/20
* Max iterations: 1000
* Evaluation metrics:

  * Accuracy Score
  * Confusion Matrix
  * Classification Report

---

## 📊 Model Performance

* Accuracy: ~78–79%
* Key insight:

  * Customers using **Fiber Optic internet** and **Electronic check payments** are more likely to churn.

---

## 📁 Project Structure

```
Customer-Churn-Prediction/
│
├── data/
│   └── churn.csv
│
├── notebooks/
│   └── churn_prediction.ipynb
│
├── models/
│   └── churn_model.pkl
│
├── requirements.txt
└── README.md
```

---

## 🚀 How to Run This Project

### 1. Clone Repository

```bash
git clone https://github.com/your-username/Customer-Churn-Prediction.git
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Notebook

Open Jupyter Notebook and run:

```
churn_prediction.ipynb
```

---

## 📈 Future Improvements

* Use advanced models (Random Forest, XGBoost)
* Hyperparameter tuning
* Deploy using Streamlit or Flask
* Improve feature engineering

---

## 📌 Author

**Fathima Luluh**

---

## 📜 License

This project is open-source and free to use for learning purposes.
