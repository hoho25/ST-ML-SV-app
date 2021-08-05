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


# ---------------------------------------------------------------------------- #

main_app = dill.load(open('main-app.pkl', 'rb'))

if __name__ == '__main__':
    main_app()
