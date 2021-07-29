########################
### Import Libraries ###
########################
# EDA Libraries
import numpy as np
import pandas as pd

# Visualization Libraries
from statistics import mode
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns

# Core Libraries
import streamlit as st
import dill
from PIL import Image

# Sweetviz Libraries
import sweetviz as sv 
import codecs
import streamlit.components.v1 as components


# streamlit run ST-ML-SV-app.py

# ---------------------------------------------------------------------------- #

###################
### Page layout ###
###################

st.set_page_config(page_title = "Don's App", page_icon = "👩‍✈️",
                   layout = "wide", initial_sidebar_state = "expanded")  # Page expands to full width


pages = ['Overview', 'Streamlit Introduction 👑', 'Machine Learning 🤖', 'Data Visualization (SweetViz) 📊']
option = st.sidebar.selectbox('Select a Web App Demo', pages, 0) # Preselect Overview
    

# ---------------------------------------------------------------------------- #
#############################
### Page 1: Overview Page ###
#############################
if option == 'Overview':
    # Title
    st.balloons()
    st.title("Welcome to my page! 🎉🎊")
    st.subheader("**Author: ©️ Ho Yie Don 👩‍✈️💻**")
    st.write('Before you continue, please read the [terms and conditions](https://www.gnu.org/licenses/gpl-3.0.en.html)')

    if st.checkbox('I agree the terms and conditions.'):
        st.markdown("""---
## About 🎈
The purpose of this Web Application is to demonstrate the following:\n
(Coded in **Python Version 3.8.10**)\n
**1. Introduction to Streamlit Library 👑**
  - **Display**: Text, Status, Progress, Interactive Widgets, Media
 
**2. Supervised Machine Learning (Categorical Label) 🤖**
  - **Dataset:** Default / User-Defined
  - **Model:** Logistic Regression, KNN, SVM, Gaussian NB, Random Forest, Gradient Boosting, Ada Boosting
  - **Evaluation Metrics:** Confusion Matrix, Classification Report, ROC Curve, Precision-Recall Curve, 
Prediction Probability, Coefficient, Feature Importances

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
    st.sidebar.write('Before you continue, please read the [terms and conditions](https://www.gnu.org/licenses/gpl-3.0.en.html)')
    if st.sidebar.checkbox('I agree the terms and conditions.'):
        st.sidebar.markdown("---")
        load_streamlit_intro = dill.load(open('st-intro.pkl', 'rb'))
        load_streamlit_intro()
        
        
# ---------------------------------------------------------------------------- #
################################
### Page 3: Machine Learning ###
################################  
elif option == "Machine Learning 🤖":
    st.sidebar.write('Before you continue, please read the [terms and conditions](https://www.gnu.org/licenses/gpl-3.0.en.html)')
    if st.sidebar.checkbox('I agree the terms and conditions.'):
        st.sidebar.markdown("---")
        dataset = st.sidebar.radio("Choose a Dataset", ["Default", "User-Defined"])
        
        # ----------------------------------------------------------------------- #
        #########################
        ### Page 3.1 Overview ###
        #########################
        if dataset == "Default":
            def_option = st.sidebar.selectbox("Select Default Dataset", ["Overview", "Iris 🌷", "Penguin 🐧"])
            
            ### Page 3.1.1 Overview
            if def_option == "Overview":
                # Logo
                image = Image.open('ml-logo.png')
                st.image(image, use_column_width = True)
                
                # Title
                st.title('Machine Learning: Classification 🤖')
                st.markdown("""## About 🎈
This app performs Machine Learning Predictions for Classification Label!
* **Default Dataset:** Iris Flower 🌷, Palmer Penguin 🐧
* **Note:** The Datasets were cleaned internally. (No missing values)
* **Python libraries:** numpy, pandas, matplotlib, seaborn, sklearn, streamlit
* **Author:** ©️ Ho Yie Don 👩‍✈️💻""")

            ### Page 3.1.2 Iris
            elif def_option == "Iris 🌷":
                load_iris_dataset = dill.load(open('default-iris-ML-app.pkl', 'rb'))
                load_iris_dataset()
            
            ### Page 3.1.3 Penguin
            elif def_option == "Penguin 🐧":
                load_penguin_dataset = dill.load(open('default-penguin-ML-app.pkl', 'rb'))
                load_penguin_dataset()
        
        # ----------------------------------------------------------------------- #
        #############################
        ### Page 3.2 User-Defined ###
        #############################
        elif dataset == "User-Defined":
            # Logo
            image = Image.open('ml-logo2.jpg')
            # image = Image.open('sklearn-logo.png')
            st.image(image, use_column_width = True)
            
            # Title + Markdown
            st.title('Machine Learning: Classification 👨‍🏫')
            st.markdown("""## About 🎈
This app performs machine learning predictions for classification label!
(Support Binary Classification / Multi-Class Classification)
* **Python libraries:** numpy, pandas, statistics, matplotlib, seaborn, sklearn, streamlit
* **Author:** ©️ Ho Yie Don 👩‍✈️💻
---""")
        
            # Upload User File
            uploaded_file = st.sidebar.file_uploader("Upload your input CSV file 📂📄", type=["csv"])
            st.sidebar.info("""**💡 Note:**\nKindly clear the previous file by clicking the 'X' before browsing a new file""")
            
            help_index_col = """**💡 Note:** Select the column number as index (if any).\n
**Hint:** It is recommended to select **'0'** if the first column of dataframe is **'Unnamed: 0'**."""
            index_col = st.sidebar.radio("Index Column", [None, 0, 1, 2], help = help_index_col) # Preselect index_col = None
            sep = st.sidebar.radio("File Seperator", [',', ':', ';', '/'])  # Preselect sep = ','
                
            if uploaded_file is not None:
                df = pd.read_csv(uploaded_file, header = 0, index_col = index_col, sep = sep, skipinitialspace = True)
                
                load_user_defined = dill.load(open('user-defined-ML-app.pkl', 'rb'))
                load_user_defined(df)
                
            else:
                st.write('Awaiting CSV file to be uploaded... ⏳')
                st.markdown("![GIF](https://media.giphy.com/media/l1AsVPJml2RsaMFuU/giphy.gif)")
    

# ---------------------------------------------------------------------------- #
########################
### Page 4: Sweetviz ###
########################
elif option == "Data Visualization (SweetViz) 📊":
    st.sidebar.write('Before you continue, please read the [terms and conditions](https://www.gnu.org/licenses/gpl-3.0.en.html)')
    if st.sidebar.checkbox('I agree the terms and conditions.'):
        st.sidebar.markdown("---")
        load_sweetviz_app = dill.load(open('sv-app.pkl', 'rb'))
        load_sweetviz_app()


