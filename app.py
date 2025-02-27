from mlflow import Image
import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
from streamlit_option_menu import option_menu

def load_model():
    with open("knn_model.pkl", "rb") as file:
        model = pickle.load(file)
    return model

def main():
    st.title("📱 Mobile Usage Analytics & Prediction Dashboard")
    
    # Sidebar menu
    with st.sidebar:
        menu = option_menu("Navigation", ["Overview", "Usage Analysis", "Predict Primary Use"],
                           icons=["house", "bar-chart", "search"], menu_icon="cast", default_index=0)
    
    model = load_model()
    category_mapping = {0: "Education", 1: "Gaming", 2: "Entertainment", 3: "Social Media", 4: "Work"}
    
    if menu == "Overview":
        st.write("Decoding Phone Usage Patterns in India")
        st.write("An analysis of mobile usage trends across different cities in India.")

        st.header("📝 Project Overview")
        st.write("This project aims to analyze mobile device usage patterns in India, leveraging data analysis, machine learning, and clustering techniques. It provides insights into user behavior, device preferences, and primary usage trends, ultimately offering valuable insights for businesses, manufacturers, and consumers.")

        st.header("🎯 Key Objectives")
        st.markdown("""
        - Analyze user behavior through mobile usage metrics.
        - Classify users based on primary device usage.
        - Cluster users based on their device usage patterns.
        - Visualize trends using Exploratory Data Analysis (EDA).
        - Deploy an interactive application using Streamlit.
        """)

        st.header("🏗️ Tech Stack & Skills Used")
        st.markdown("""
        - **Programming:** Python
        - **Data Analysis:** Pandas, NumPy, Matplotlib, Seaborn
        - **Machine Learning:** Scikit-learn, XGBoost
        - **Clustering Techniques:** K-Means, DBSCAN
        - **Deployment:** Streamlit
        """)

        st.header("📂 Dataset Description")
        st.markdown("""
        The dataset contains the following key features:

        - **User Demographics:** Age, Gender, Location
        - **Device Information:** Phone Brand, OS (Android/iOS)
        - **Usage Metrics:**
        - Screen Time (hrs/day)
        - Data Usage (GB/month)
        - Calls Duration (mins/day)
        - Number of Installed Apps
        - Social Media, Streaming & Gaming Time
        - Monthly Recharge Cost (INR)
        - **Primary Use:** Education, Gaming, Entertainment, Social Media
        """)

        st.header("🔍 Approach")
        st.markdown("""
        - **Data Preparation & Cleaning**
        - Handling missing values, outliers, and standardizing formats.
        - **Exploratory Data Analysis (EDA)**
        - Analyzing trends in screen time, battery usage, and app installations.
        - **Machine Learning & Clustering**
        - Classification models: Logistic Regression, Decision Trees, Random Forest, XGBoost, KNN.
        - Clustering methods: K-Means, DBSCAN.
        - **Application Development**
        - Creating an interactive Streamlit dashboard.
        - **Deployment**
        - Making the application accessible to end-users.
        """)

    elif menu == "Usage Analysis":
        st.write("### Data Insights & Visualization")

        st.subheader("Average Screen Time by Gender")
        image = Image.open("gender.png")
        resized_image = image.resize((800, 500))
        st.image(resized_image)
        st.text("According to the bar plot, the screen time for males and females is almost similar.")

        st.write("---")

        st.subheader("Operating System Distribution")
        image = Image.open("OS_device.png")
        resized_image = image.resize((800, 600))
        st.image(resized_image)
        st.text("According to the pie chart, 90% of users use Android, while the remaining users use iOS.")

        st.write("---")

        st.subheader("Apple and Samsung user by Location")
        image = Image.open("phone_brand_location.png")
        resized_image = image.resize((800, 600))
        st.image(resized_image)
        st.text("""In most cities, such as Pune, Mumbai, Chennai, Bangalore, Ahmedabad, and Delhi, 
                Samsung users are more prevalent, while in the remaining cities, Apple users are more common.""")

        st.write("---")

        st.subheader("Delivery Time Distibution over Data")
        image = Image.open("phone_usage_phone_brand.png")
        resized_image = image.resize((800, 600))
        st.image(resized_image)
        # st.text("According to the histogram plot, delivery agents often take between 60 and 160 minutes for deliveries.")

        st.write("---")

        st.subheader("Delivery Time Distibution over Data")
        image = Image.open("phone_usage.png")
        resized_image = image.resize((800, 600))
        st.image(resized_image)
        # st.text("According to the histogram plot, delivery agents often take between 60 and 160 minutes for deliveries.")

        st.write("---")

        st.subheader("Delivery Time Distibution over Data")
        image = Image.open("purpose_phone.png")
        resized_image = image.resize((800, 600))
        st.image(resized_image)
        # st.text("According to the histogram plot, delivery agents often take between 60 and 160 minutes for deliveries.")

        st.write("---")
        
    elif menu == "Predict Primary Use":
        st.write("### Predict the Primary Use of a Mobile User")
        
        age = st.number_input("Age", min_value=10, max_value=100, step=1)
        scr_time = st.number_input("Screen Time (hours/day)", min_value=0.0, step=0.1)
        data_usage = st.number_input("Data Usage (GB/month)", min_value=0.0, step=0.1)
        calls_dur = st.number_input("Calls Duration (min/day)", min_value=0.0, step=0.1)
        installed_apps = st.number_input("Installed Apps", min_value=0)
        social_media = st.number_input("Social Media Usage (hours/day)", min_value=0.0, step=0.1)
        ecom_spent = st.number_input("E-Commerce Spending (INR/month)", min_value=0)
        streaming = st.number_input("Streaming Hours (hours/day)", min_value=0.0, step=0.1)
        gaming = st.number_input("Gaming Hours (hours/day)", min_value=0.0, step=0.1)
        recharge = st.number_input("Recharge Amount (INR)", min_value=0)
        
        if st.button("Predict Usage Category"):
            input_data = pd.DataFrame([[age, scr_time, data_usage, calls_dur, installed_apps, social_media, ecom_spent, streaming, gaming, recharge]],
                                      columns=["Age", "Scr_time(h/d)", "data_usage(gb/mo)", "calls_dur(min/d)", "installed_apps", "soical_media(h/d)", "E-commerce(INR/m)", "streaming(hrs/d)", "gaming(hrs/d)", "recharge(INR)"])
            prediction = model.predict(input_data)[0]
            predicted_category = category_mapping.get(prediction, "Unknown")
            st.success(f"Predicted Primary Use: {predicted_category}")
            
if __name__ == "__main__":
    main()
