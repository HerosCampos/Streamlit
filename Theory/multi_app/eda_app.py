import streamlit as st
import pandas as pd


def run_eda_app():
    st.subheader("From Exploratory Data Analysis")
    df = pd.read_csv("Data/diabetes.csv")
    st.dataframe(df)



















































