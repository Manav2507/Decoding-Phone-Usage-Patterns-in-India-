# 📱 Decoding Phone Usage Patterns in India

An analytical project exploring mobile device usage across Indian cities. It combines data preprocessing, clustering, and classification to reveal user behavior and device preferences. Features an interactive Streamlit dashboard for exploring insights.

---
## Demo ScreenShots

![Picture](https://github.com/Manav2507/Decoding-Phone-Usage-Patterns-in-India-/blob/main/5_1.png)
![Picture](https://github.com/Manav2507/Decoding-Phone-Usage-Patterns-in-India-/blob/main/5_2.png)
![Picture](https://github.com/Manav2507/Decoding-Phone-Usage-Patterns-in-India-/blob/main/5_3.png)

## 📌 Project Overview

This project uses real-world-like mobile usage data to:
- Understand how people in India use smartphones (apps, data, calls)
- Segment users by behavior using **ML and clustering**
- Offer actionable insights for **telecoms, marketers, manufacturers, and app developers**

---

## 🎯 Objectives

- 🔍 Analyze mobile usage patterns across user types  
- 📊 Visualize trends in usage, recharge behavior, and device type  
- 🤖 Build ML models to classify users by **primary device use**  
- 🧠 Cluster users into behavioral segments  
- 🌐 Deploy results as an interactive **Streamlit dashboard**

---

## 📂 Dataset Features

| Category          | Features                                         |
|-------------------|--------------------------------------------------|
| **Demographics**   | Age, Gender, Location                            |
| **Device Info**    | Phone Brand, OS (Android/iOS)                   |
| **Usage Metrics**  | Screen Time, Data Usage, Call Time, App Count   |
| **Engagement**     | Time spent on Social Media, Streaming, Gaming   |
| **Financial**      | Monthly Recharge (INR)                          |
| **Target**         | Primary Use (Education, Gaming, etc.)           |

---

## 🔍 Approach

### 🧹 Data Preparation
- Handled nulls, outliers, and inconsistent values  
- Normalized/standardized numerical features  

### 📊 Exploratory Data Analysis (EDA)
- App usage patterns across age groups  
- Recharge vs usage trends  
- Popularity of OS/brands across cities  

### 🧠 Machine Learning Models
| Task          | Models Used                                 |
|---------------|----------------------------------------------|
| Classification| Logistic Regression, Random Forest, XGBoost, KNN |
| Clustering    | K-Means, DBSCAN                              |

- **Target**: Predict user’s primary phone use  
- Evaluated using: Accuracy, Precision, Recall, F1-Score  

### 🖥️ App Interface (Streamlit)
- Upload your own CSV file  
- View usage distribution charts  
- Explore ML predictions and clusters  
- Cluster-wise feature insights  

---

## 🛠️ Tech Stack

| Layer             | Tools Used                            |
|-------------------|----------------------------------------|
| Programming       | Python                                 |
| Data Analysis     | Pandas, NumPy, Seaborn, Matplotlib     |
| Machine Learning  | Scikit-learn, XGBoost, KMeans, DBSCAN  |
| UI & Deployment   | Streamlit                              |

---

## 📊 Key Insights (Sample)

- Users under 25 spend more time on **gaming and social media**  
- **iOS users** tend to have higher recharge costs and fewer apps  
- A significant cluster of users has **low data + high call time** – ideal for voice plans  
- **XGBoost** outperformed other models in classifying primary usage type with ~89% F1-score  

