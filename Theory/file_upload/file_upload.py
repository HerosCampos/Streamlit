from re import I
import streamlit as st
from PIL import Image
import pandas as pd


@st.cache
def load_image(image_file):
    img = Image.open(image_file)
    return img


def main():
    st.title("File Upload Tutorial")

    menu = ['Home', 'Dataset', 'DocumentFiles', 'About']
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == 'Home':
        st.subheader('Home')
        image_file = st.file_uploader('Upload Images', type = ['png', 'jpg', 'jpeg'])
        if image_file is not None:
            st.write(type(image_file))
            # st.write(dir(image_file))
            file_details = {'filename': image_file.name,
                            'filetype': image_file.type,
                            'filesize': image_file.size}
            st.write(file_details)
            st.image(load_image(image_file), width = 250)

    elif choice == 'Dataset':
        st.subheader('Dataset')
        data_file = st.file_uploader('Upload CSV', type = ['csv'])
        if data_file is not None:
            st.write(type(data_file))
            df = pd.read_csv(data_file)
            st.dataframe(df)

    elif choice == 'DocumentFiles':
        st.subheader('DocumentFiles')
        docx_file = st.file_uploader('Upload Document', type = ['pdf', 'docx', 'txt'])
        if st.button('Process'):
            if docx_file is not None:
                file_details = {'filename': docx_file.name,
                                'filetype': docx_file.type,
                                'filesize': docx_file.size}
                st.write(file_details)
                if docx_file.type == "text/plain":
                    raw_text = docx_file.read()
                    st.write(raw_text)

    else:
        st.subheader('About')








if __name__ == '__main__':
    main()










































































