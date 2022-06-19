import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")
import seaborn as sns
import plotly.express as px




def main():
    st.title("Plotting with st.pyplot")
    df = pd.read_csv('../iris.csv')
    st.dataframe(df)

    #####################################
    # Matplotlib & Seaborn
    #####################################

    # fig = plt.figure()
    # df['species'].value_counts().plot(kind = 'bar')
    # st.pyplot(fig)

    # fig, ax = plt.subplots()
    # df['species'].value_counts().plot(kind = 'bar')
    # st.pyplot(fig)

    # fig = plt.figure()
    # sns.countplot(df['species'])
    # st.pyplot(fig)



    #####################################
    # Plotly
    #####################################
    st.title("Plotting in Streamlit with Plotly")
    df = pd.read_csv('../file_upload/prog_languages_data.csv')
    st.dataframe(df)

    fig = px.pie(df, values = 'Sum', names = 'lang', title = 'Pie Chart of Languages')
    st.plotly_chart(fig)

    fig2 = px.bar(df, x = 'lang', y = 'Sum')
    st.plotly_chart(fig2)







if __name__ == '__main__':
    main()



















































