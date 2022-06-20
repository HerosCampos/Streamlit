from configparser import Interpolation
import streamlit as st
import neattext.functions as nfx
from wordcloud import WordCloud
from collections import Counter
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import altair as alt
import pandas as pd
from textblob import TextBlob



def plot_wordcloud(docx):
    mywordcloud = WordCloud().generate(docx)
    fig = plt.figure(figsize = (20, 10))
    plt.imshow(mywordcloud, interpolation = 'bilinear')
    plt.axis('off')
    st.pyplot(fig)

def plot_word_freq(docx, num = 10):
    word_freq = Counter(docx.split())
    most_common_tokens = word_freq.most_common(num)
    x, y = zip(*most_common_tokens)
    fig = plt.figure(figsize = (20, 10))
    plt.bar(x, y)
    plt.xticks(rotation = 45, fontsize = 100)
    plt.yticks(fontsize = 100)
    plt.show()
    st.pyplot(fig)

def plot_mendelhall_curve(docx):
    word_length = [len(token) for token in docx.split()]
    word_length_count = Counter(word_length)
    sorted_word_length_count = sorted(dict(word_length_count).items())
    x, y = zip(*sorted_word_length_count)
    mendelhall_df = pd.DataFrame({"tokens": x, 'counts': y})
    st.line_chart(mendelhall_df['counts'])

def get_pos_tags(docx):
    blob = TextBlob(docx)
    tagged_docx = blob.tags
    tagged_df = pd.DataFrame(tagged_docx, columns = ['token', 'tags'])
    return tagged_df



def main():
    st.title('Text Analysis App')
    menu = ['Home', 'About']
    choice = st.sidebar.selectbox('Menu', menu)


    if choice == 'Home':
        st.subheader('Home')
        raw_text = st.text_area('Enter text here:')

        if st.button("Submit"):
            if len(raw_text) >= 2:
                st.success("Success")
            elif len(raw_text) == 1:
                st.warning("Insufficient text, minimum is 2!")
            else:
                st.write("Enter text")
        
        col1, col2 = st.columns(2)
        processed_text = nfx.remove_stopwords(raw_text)

        with col1:
            with st.expander("Original Text"):
                st.write(raw_text)
            
            with st.expander('PoS Tagged Text'):
                tagged_docx = get_pos_tags(raw_text)
                st.dataframe(tagged_docx)

            with st.expander('Plot Word Freq'):
                plot_word_freq(processed_text)

        with col2:
            with st.expander("Processed Text"):
                
                st.write(processed_text)

            with st.expander('Plot Wordcloud'):
                st.success('Wordcloud')
                plot_wordcloud(processed_text)

            with st.expander('Plot Stylometry Curve'):
                plot_mendelhall_curve(processed_text)






    else:
        st.subheader('About')







if __name__ == '__main__':
    main()



