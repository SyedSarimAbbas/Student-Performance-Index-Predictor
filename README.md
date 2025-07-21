#  Student Performance Index Prediction App

This is a Machine Learning-based web application that predicts a **Student Performance Index** based on various input parameters such as academic scores, sleep hours, study hours, and more. The model is deployed using **Streamlit**, allowing users to interact with the model through a clean and responsive web interface.

---

##  Overview

This project demonstrates how Machine Learning can be used to assess and predict student academic outcomes. The model was trained using a dataset containing student attributes like previous scores, sample practice paper , and sleeping hours details. By using a regression algorithm, the model outputs a **Performance Index Score** which can help in early identification of students needing academic support.

---

## Machine Learning Strategy

-  **Data Collection**: A dataset of student attributes was collected and loaded using **pandas**.
-  **Data Preprocessing**:
  - Handled missing values
  - Converted categorical features using label encoding or one-hot encoding
  - Normalized numerical features
-  **Model Selection**:
  - Initial model: **Linear Regression**
  - Improved performance using **Random Forest Regressor** and **Polynomial Regression**
-  **Model Evaluation**:
  - R² Score
  - Mean Absolute Error (MAE)
  - Root Mean Squared Error (RMSE)
-  **Model Saving**: Trained model saved as `model.pkl` using `pickle` for deployment

---

## 🧰 Tech Stack & Libraries

- **Python 3.x**
- **Pandas** – for data analysis
- **NumPy** – for numerical operations
- **Scikit-learn** – for ML model training and evaluation
- **Matplotlib / Seaborn** – for visualization (optional)
- **Streamlit** – for building the interactive web interface
- **Pickle** – to serialize the trained ML model

---
