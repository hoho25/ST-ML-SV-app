########################
### Import Libraries ###
########################
# Core Libraries
import streamlit as st
import dill
from PIL import Image

# EDA Libraries
import numpy as np
import pandas as pd

# Visualization Libraries
from statistics import mode
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns

# Sweetviz Libraries
import sweetviz as sv 
import codecs
import streamlit.components.v1 as components


# streamlit run ST-ML-SV-app.py

# ---------------------------------------------------------------------------- #

def main():
    """Streamlit - Machine Learning - SweetViz App"""

    ###################
    ### Page layout ###
    ###################
    st.set_page_config(page_title = "Don's App", page_icon = "👩‍✈️",
                       layout = "wide", initial_sidebar_state = "expanded")  # Page expands to full width
    
    ###########################
    ### User Login / SignUp ###
    ###########################
    load_login = dill.load(open('login.pkl', 'rb'))
    access = load_login()

    if access:
        pages = ['Overview', 'Streamlit Introduction 👑', 'Machine Learning 🤖', 'Data Visualization (SweetViz) 📊']
        option = st.sidebar.selectbox('Select a Web App Demo', pages, 0) # Preselect Overview
            
        
        # ---------------------------------------------------------------------------- #
        #############################
        ### Page 1: Overview Page ###
        #############################
        if option == 'Overview':
            # Logo
            image = Image.open('page-logo2.jpg')
            st.image(image, use_column_width = True)
            
            # Title
            st.balloons()
            st.title("Welcome to my page! 🎉🎊")
            st.subheader("**Author: ©️ Ho Yie Don 👩‍✈️💻**")
            st.markdown("""## About 🎈
The purpose of this Web Application is to demonstrate the following:\n
(Coded in **Python Version 3.8.10**)\n
**1. Introduction to Streamlit Library 👑**
  - **Display**: Text, Status, Progress, Interactive Widgets, Media
 
**2. Machine Learning 🤖**\n

**Part I. Supervised Learning (Classification / Regression)**
  - **Dataset:** Default / User-Defined
  - **Model:** Linear Regression, Logistic Regression, KNN, SVM, Gaussian NB, Random Forest, Gradient Boosting, Ada Boosting
  - **Evaluation Metrics for Classification:** Confusion Matrix, Classification Report, ROC Curve, Precision-Recall Curve, 
Prediction Probability, Coefficient, Feature Importances
  - **Evaluation Metrics for Regression:** MAE, MSE, RMSE, R^2

**Part II. Unsupervised Learning (Clustering)**
  - **Dataset:** Default / User-Defined
  - **Model:** KMeans
  - **Evaluation Metrics:** Sum of Squared Distances (SSD) Reduction
  
**3. Data Visualtion (Sweetviz) 📊**
  - **Options:** Analysis, Comparison 
    
**Disclaimer:** All media rights are reserved to their respective owners. If I happen to infringe or owners
do not want to be featured, please do not hesitate to contact me so that I can take it down as soon as possible.""")
            st.markdown("---")
            st.sidebar.info("**Info:** Please click the arrow above to select the option")
            
            # Self Introduction
            expander_bar = st.beta_expander('📌 Self Introduction 👩‍✈️💻')
            with expander_bar:
                image = Image.open('my-photo.jpeg')
                st.image(image, width = 500)
                st.write("The year 2020 was supposed to be the year I started my flying career in [AirAsia](https://www.airasia.com/en/gb). \
However, due to the pandemic, my career had taken an unexpected turn and my training had to be temporarily \
put on hold until further notice. Midway during the pandemic, I came to realize how vital IT-related skills \
are in the functioning of our modern society today. Since Oct 2020, I decided to pick up coding in Python during \
my free time to gain an additional skill and exposure in IT. Shortly after, I took the opportunity to join\
AirAsia’s [Red Beat Academy](https://redbeatacademy.com/) full fledged course in [Data Analytics](https://redbeatacademy.com/course/data-analytics-complete-reskill-program) \
to further upskill my skillset together with the possibility to further apply the knowledge in an active \
supporting role within AirAsia. I would like to give my sincere appreciation to all RBA instructors/management \
and especially to Dr. Yu Yong Poh for all his guidance throughout the data analytics course.")
        
            # Feedback
            url = "https://forms.gle/4gnRvjkjaiw7KG1d9"
            expander_bar = st.beta_expander('📌 Feedback 📝')
            with expander_bar:
                st.write("You may fill up the feedback form below if you have any comment or found any bug. \
Your response is greatly appreciated! 😊")
                st.components.v1.iframe(url, width = 700, height = 1400)
            
            
        # ---------------------------------------------------------------------------- #
        ###################################### 
        ### Page 2: Streamlit Introduction ###
        ###################################### 
        elif option == "Streamlit Introduction 👑":
            load_streamlit_intro = dill.load(open('st-intro.pkl', 'rb'))
            load_streamlit_intro()
                
                
        # ---------------------------------------------------------------------------- #
        ################################
        ### Page 3: Machine Learning ###
        ################################  
        elif option == "Machine Learning 🤖":
            st.sidebar.markdown("---")
            choice = ["Overview", "Supervised Learning", "Unsupervised Learning"]
            ml_type = st.sidebar.selectbox("Select a type of Machine Learning", choice, 0) # Preseletct "Supervised Learning"
            
            if ml_type == "Overview":
                # Logo
                image = Image.open('ml-logo-ov.jpg')
                st.image(image, use_column_width = True)
                
                # Title
                st.title("Machine Learning 🤖")
                st.subheader("**Author: ©️ Ho Yie Don 👩‍✈️💻**")
                st.markdown("""## About 🎈
### Supervised Machine Learning
1. Classification:
  - **Dataset:** Default (Iris Flower 🌷, Palmer Penguin 🐧) / User-Defined 👨‍🏫
  - **Model:** Logistic Regression, KNN, SVM, Gaussian NB, Random Forest, Gradient Boosting, Ada Boosting
  - **Evaluation Metrics:** Confusion Matrix, Classification Report, ROC Curve, Precision-Recall Curve, 
Prediction Probability, Coefficient, Feature Importances
2. Regression
  - **Dataset:** Default (Boston House 🏡) / User-Defined 👨‍🏫
  - **Model:** Linear Regression, KNN, SVM, Gaussian NB, Random Forest, Gradient Boosting, Ada Boosting
  - **Evaluation Metrics:** MAE, MSE, RMSE, R^2
### Unsupervised Machine Learning
3. Clustering
  - **Dataset:** Default (Wine 🍷) / User-Defined 👨‍🏫
  - **Model:** KMeans
  - **Evaluation Metrics:** Sum of Squared Distances (SSD) Reduction
---""")
            
            ####################################
            ### Type 3.1 Supervised Learning ###
            ###################################
            elif ml_type == "Supervised Learning":
                sup_type = ["Classification", "Regression"]
                sup_type = st.sidebar.selectbox("Select a type of Supervised Learning", sup_type, 0) # Preseletct "Classification"
                
                ############################
                ### 3.1.1 Classification ###
                ############################
                if sup_type == "Classification":  
                    dataset = st.sidebar.radio("Choose a Dataset", ["Default", "User-Defined"], key = "class")
                    
                    # ----------------------------------------------------------------------- #
                    ### 3.1.1.1 Default Dataset
                    if dataset == "Default":
                        def_option = st.sidebar.selectbox("Select Default Dataset", ["Overview", "Iris 🌷", "Penguin 🐧"], key = "class_def")
                        
                        ### 3.1.1.1.1 Overview
                        if def_option == "Overview":
                            # Logo
                            image = Image.open('ml-logo.png')
                            st.image(image, use_column_width = True)
                            
                            # Title
                            st.title('Supervised Machine Learning: Classification 🤖')
                            st.markdown("""## About 🎈
This app performs Supervised Machine Learning Predictions for Classification Label!
* **Default Dataset:** Iris Flower 🌷, Palmer Penguin 🐧
* **Note:** The Datasets were cleaned internally. (No missing values)
* **Python libraries:** numpy, pandas, matplotlib, seaborn, sklearn, streamlit
* **Author:** ©️ Ho Yie Don 👩‍✈️💻
---""")
            
                        ### 3.1.1.1.2 Iris
                        elif def_option == "Iris 🌷":
                            load_iris_dataset = dill.load(open('default-iris-ML-app.pkl', 'rb'))
                            load_iris_dataset()
                        
                        ### 3.1.1.1.3 Penguin
                        elif def_option == "Penguin 🐧":
                            load_penguin_dataset = dill.load(open('default-penguin-ML-app.pkl', 'rb'))
                            load_penguin_dataset()
                            
                    # ----------------------------------------------------------------------- #
                    ### 3.1.1.2 User-Defined
                    elif dataset == "User-Defined":
                        load_user_defined_class = dill.load(open('user-defined-ML-Class-app.pkl', 'rb')) 
                        load_user_defined_class()
                
                
                # ----------------------------------------------------------------------- #
                ########################
                ### 3.1.2 Regression ###
                ########################
                if sup_type == "Regression":  
                    dataset = st.sidebar.radio("Choose a Dataset", ["Default", "User-Defined"], key = "reg")
                    
                    # ----------------------------------------------------------------------- #
                    ### 3.1.2.1 Default Dataset
                    if dataset == "Default":
                        def_option = st.sidebar.selectbox("Select Default Dataset", ["Overview", "Boston 🏡"], key = "reg_def")
                        
                        ### 3.1.2.1.1 Overview
                        if def_option == "Overview":
                            # Logo
                            image = Image.open('ml-logo.png')
                            st.image(image, use_column_width = True)
                            
                            # Title
                            st.title('Supervised Machine Learning: Regression 🤖')
                            st.markdown("""## About 🎈
This app performs Supervised Machine Learning Predictions for Continuous Label!
* **Default Dataset:** Boston House 🏡
* **Note:** The Dataset was cleaned internally. (No missing values)
* **Python libraries:** numpy, pandas, matplotlib, seaborn, sklearn, streamlit
* **Author:** ©️ Ho Yie Don 👩‍✈️💻
---""")
            
                        ### 3.1.2.1.2 Boston
                        elif def_option == "Boston 🏡":
                            load_boston_dataset = dill.load(open('default-boston-ML-app.pkl', 'rb'))
                            load_boston_dataset()
                            
                    # ----------------------------------------------------------------------- #
                    ### 3.1.2.2 User-Defined
                    elif dataset == "User-Defined":
                        load_user_defined_reg = dill.load(open('user-defined-ML-Reg-app.pkl', 'rb'))
                        load_user_defined_reg()   
                    
            # ----------------------------------------------------------------------- #        
            ######################################
            ### Type 3.2 Unsupervised Learning ###
            ######################################
            elif ml_type == "Unsupervised Learning":
                unsup_type = ["Clustering"]
                unsup_type = st.sidebar.selectbox("Select a type of Unsupervised Learning", unsup_type, 0) # Preseletct "Classification"
                
                ########################
                ### 3.2.1 Clustering ###
                ########################
                if unsup_type == "Clustering":  
                    dataset = st.sidebar.radio("Choose a Dataset", ["Default", "User-Defined"], key = "clust")
                    # load_overview_clust, load_user_defined_clust = dill.load(open('user-defined-ML-Cluster-app.pkl', 'rb')) 
                    
                    # ----------------------------------------------------------------------- #
                    ### 3.1.1.1 Default Dataset
                    if dataset == "Default":
                        def_option = st.sidebar.selectbox("Select Default Dataset", ["Overview", "Wine 🍷"], key = "clust_def")
                          
                        ### 3.1.1.1.1 Overview
                        if def_option == "Overview":
                            # Logo
                            image = Image.open('ml-logo.png')
                            st.image(image, use_column_width = True)
                            
                            # Title
                            st.title('Unsupervised Machine Learning: Clustering 🤖')
                            st.markdown("""## About 🎈
This app performs Unsupervised Machine Learning for Clustering Label!
* **Default Dataset:** Wine 🍷
* **Note:** The Datasets were cleaned internally. (No missing values)
* **Python libraries:** numpy, pandas, matplotlib, seaborn, sklearn, streamlit
* **Author:** ©️ Ho Yie Don 👩‍✈️💻
---""")
            
                        ### 3.1.1.1.2 Iris
                        elif def_option == "Wine 🍷":
                            load_wine_dataset = dill.load(open('default-wine-ML-app.pkl', 'rb'))
                            load_wine_dataset()
                        
                    # ----------------------------------------------------------------------- #
                    ### 3.1.1.2 User-Defined
                    elif dataset == "User-Defined":
                        load_user_defined_clust = dill.load(open('user-defined-ML-Cluster-app.pkl', 'rb')) 
                        load_user_defined_clust()
                
              
        # ---------------------------------------------------------------------------- #
        ########################
        ### Page 4: Sweetviz ###
        ########################
        elif option == "Data Visualization (SweetViz) 📊":
            st.sidebar.markdown("---")
            load_sweetviz_app = dill.load(open('sv-app.pkl', 'rb'))
            load_sweetviz_app()


if __name__ == '__main__':
    main()
