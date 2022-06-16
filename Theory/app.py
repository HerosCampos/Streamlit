from email.policy import default
import streamlit as st
import pandas as pd
from PIL import Image


#############################################################
# st.title("This is the Title")
# st.header('This is the Header')
# st.subheader('This is the Subheader')
# st.text('This is the text!')
# st.markdown("# Markdown 1")
# st.markdown("## Markdown 2")
# st.markdown("### Markdown 3")


#############################################################
# # Displaying Colored Text/Bootstraps Alert
# st.success("Success...")
# st.info("Info...")
# st.warning("Warning...")
# st.error("Error...")
# st.exception("Exception...")


#############################################################
# # Super Function
# st.write("# This is a text with markdown")
# st.write(1 + 2)


#############################################################
# Help Info
# st.help(range)


#############################################################
# # Display Data
# df = pd.read_csv('iris.csv')

# # Method 1
# st.dataframe(df)

# # Adding Style from Pandas
# st.dataframe(df.style.highlight_max(axis = 0))

# # Method 2 - Static Table
# st.table(df)

# # Method 3 
# st.write(df)

# # Display Json
# st.json({"data": "name"})

# # Display Code
# mycode = """
# def sayhello():
#     print('Hello Streamlit')
# """
# st.code(mycode, language = 'python')


#############################################################
# # Working with Widgets - Buttons / Radio / Checkbox / Select
# # Buttons
# name = "HEROS"

# if st.button("Click here"):
#     st.write(f'Hello, {name.capitalize()}!')

# if st.button("Click here", key = 'new02'):
#     st.write(f'You are awesome, {name.capitalize()}!')

# # Radio Buttons
# status = st.radio("What is your status?", ('Active', 'Inactive'))

# if status == 'Active':
#     st.success("You are active!")
# else:
#     st.warning("You are inactive!")

# # Checkbox
# if st.checkbox('Show/Hide'):
#     st.text('Showing Something')

# # Expander
# with st.expander("See explanation"):
#      st.write("""
#          Explanation here!
#      """)

# # Select
# my_lang = ['Python', 'C++', 'JavaScript', 'C']

# # Select Box
# choice = st.selectbox('Language', my_lang)
# st.write(f'You selected {choice}')

# # Multiple Selection
# languages = ('Python', 'C++', 'JavaScript', 'C')
# lang = st.multiselect(f'Spoken lang', languages, default = ('Python', 'C++'))

# Slider
# age = st.slider('Age', 1, 100)
# color = st.select_slider("Choose color", options = ['Red', 'Yellow', 'Blue', 'White', 'Black'], value = ['Red', 'Yellow'])


#############################################################
# # Working Media Files (Videos/Images/Audio)
# # Images
# img = Image.open("data/image_03.jpg")
# st.image(img, use_column_width = True)

# # From URL
# st.image("https://media.moneytimes.com.br/uploads/2021/07/binance-dolar-bitcoin.jpg")

# # Display Videos
# video_file = open('data/secret_of_success.mp4', 'rb').read()
# st.video(video_file)

# # Play Audio
# audio_file = open("data/song.mp3", 'rb')
# st.audio(audio_file)


#############################################################





































