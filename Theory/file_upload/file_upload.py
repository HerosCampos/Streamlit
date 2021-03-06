from curses import raw
from re import I
import streamlit as st
from PIL import Image
import pandas as pd
import docx2txt
import textract
from PyPDF2 import PdfFileReader
import pdfplumber
import os



@st.cache
def load_image(image_file):
    img = Image.open(image_file)
    return img


def save_uploaded_file(uploadedfile):
    with open(os.path.join("tempDir", uploadedfile.name), "wb") as f:
        f.write(uploadedfile.getbuffer())
    return st.success(f'Saved file {uploadedfile.name} in tempDir')


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

            with open(image_file.name, "wb") as f:
                f.write(image_file.getbuffer())
            st.success("File Saved")

    elif choice == 'Dataset':
        st.subheader('Dataset')
        data_file = st.file_uploader('Upload CSV', type = ['csv'])
        if data_file is not None:
            st.write(type(data_file))
            df = pd.read_csv(data_file)
            st.dataframe(df)
            save_uploaded_file(data_file)

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
                    # raw_text = docx_file.read()
                    # st.write(raw_text)
                    # st.text(raw_text)

                    raw_text = str(docx_file.read(), 'utf-8')
                    st.write(raw_text)

                elif docx_file.type == "application/pdf":
                    try:
                        with pdfplumber.open(docx_file) as pdf:
                            pages = pdf.pages[0]
                            st.write(pages.extract_text())
                    except:
                        st.write('None')

                else:
                    raw_text = docx2txt.process(docx_file)
                    st.write(raw_text)
                    # st.text(raw_text)


    else:
        st.subheader('About')








if __name__ == '__main__':
    main()











































































