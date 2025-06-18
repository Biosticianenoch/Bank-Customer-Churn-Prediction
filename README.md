
# 🏦 Bank Customer Churn Prediction App

[![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-ff4b4b.svg?logo=streamlit)](https://streamlit.io)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

> A smart machine learning web app to predict if a bank customer is likely to leave, enabling proactive retention strategies for banks and financial institutions.

---

## 🔮 Demo

🚀 **Live App**: [Launch on Streamlit Cloud](https://your-streamlit-url](https://bank-customer-churn-prediction-v4kgowkvuazdksvkzdsvbo.streamlit.app/)

📽️ **Video Walkthrough**: [YouTube Demo](https://youtube.com/your-demo-link)

---

## 📌 Table of Contents

- [🔧 Features](#-features)
- [📊 Input Features](#-input-features)
- [📁 Project Structure](#-project-structure)
- [⚙️ Setup & Installation](#️-setup--installation)
- [🧠 Machine Learning Pipeline](#-machine-learning-pipeline)
- [🧪 Model Performance](#-model-performance)
- [🌐 Deployment](#-deployment)
- [❓ FAQs](#-faqs)
- [💖 Support](#-support)
- [⚠️ Disclaimer](#️-disclaimer)
- [👨‍💻 Author](#-author)

---

## 🔧 Features

✅ Interactive prediction UI using Streamlit  
✅ Real-time prediction with KNN model  
✅ Label-encoded inputs for geography & gender  
✅ Clean and modern sidebar navigation  
✅ Visitor count and timestamp tracking  
✅ FAQ, disclaimer, and donation integration  
✅ Modular and production-ready code  

---

## 📊 Input Features

| Feature            | Description                                    |
|-------------------|------------------------------------------------|
| `credit_score`     | Customer’s credit score                       |
| `gender`           | Encoded: Male = 1, Female = 0                 |
| `age`              | Age in years                                  |
| `tenure`           | Years the customer has stayed with the bank  |
| `balance`          | Account balance                               |
| `products_number`  | Number of bank products                       |
| `credit_card`      | Has credit card: Yes = 1, No = 0              |
| `active_member`    | Active membership status: Yes = 1, No = 0     |
| `estimated_salary` | Customer's estimated yearly salary            |
| `country`          | Label encoded: France = 0, Spain = 1, Germany = 2 |

---

## 📁 Project Structure

```
📦 Bank Customer Churn Prediction
├── app.py                        # Streamlit app
├── bank_customer_chrun.sav      # Trained ML model (KNN)
├── visitor_data.pkl              # Auto-generated visitor data
├── README.md                     # Project documentation
├── Bank Customer Churn Prediction.pdf  # Model development report
└── requirements.txt              # Python dependencies
```

---

## ⚙️ Setup & Installation

1. **Clone the repo**
```bash
git clone https://github.com/yourusername/bank-customer-churn-app.git
cd bank-customer-churn-app
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the Streamlit app**
```bash
streamlit run app.py
```

---

## 🧠 Machine Learning Pipeline

```mermaid
graph TD
A[Load Dataset] --> B[Clean & Encode]
B --> C[Handle Imbalance (SMOTE)]
C --> D[Train-Test Split]
D --> E[Scaling (MinMax)]
E --> F[Model Training: KNN + GridSearchCV]
F --> G[Model Evaluation]
G --> H[Save model with Pickle]
```

📌 **PDF Report** available in the repo: `Bank Customer Churn Prediction.pdf`

---

## 🧪 Model Performance

| Model                | Accuracy | F1 Score |
|---------------------|----------|----------|
| ✅ Random Forest     | **95.04%** | 0.95     |
| XGBoost             | 89.77%   | 0.90     |
| KNN                 | 87.22%   | 0.88     |
| Gradient Boosting   | 86.94%   | 0.87     |
| SVM                 | 82.04%   | 0.82     |
| Voting Classifier   | 78.68%   | 0.79     |
| AdaBoost            | 77.96%   | 0.77     |
| Logistic Regression | 68.90%   | 0.69     |

---

## 🌐 Deployment

The app has been deployed on streamlit cloud to make real world predictions

- [Streamlit Cloud](https://streamlit.io/cloud)

---

## ❓ FAQs

> **Can I use this with other datasets?**  
Yes! Just ensure the new dataset has the same features or retrain the model.

> **Does this app store data?**  
No. All inputs are transient. Only visitor counts are stored locally via `visitor_data.pkl`.

> **Is the model explainable?**  
The model is interpretable using feature importance from RF/XGBoost. Integrations like SHAP can be added.

---

## 💖 Support

If you like this project and want to see more:

- 💸 Donate via **M-Pesa**: `+254701344230`
- 💳 Paybill: `522522` → Account: `1340849054`
- 📧 PayPal: `dataquestsolutions2@gmail.com`
- 🌟 Star this repo
- 🤝 Share with your community

---

## ⚠️ Disclaimer

- This app is built for educational and demonstration purposes.
- It is not intended for production without proper validation.
- All results depend on the training data and assumptions made.

---

## 👨‍💻 Author

**Biostician Enoch**  
🎓 Data Scientist | 📊 Health Analyst | 🧠 ML Enthusiast

📫 Connect:  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://linkedin.com/in/your-profile)  
[![GitHub](https://img.shields.io/badge/GitHub-Biosticianenoch-000?logo=github)](https://github.com/Biosticianenoch)

> 💡 *Transforming data into action. One prediction at a time.*
