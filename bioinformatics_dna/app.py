import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image


#####################
# Título da Página
#####################

image = Image.open("dna-logo.jpg")

st.image(image, use_column_width = True)

st.markdown("""
    # DNA Nucleotide Count Web App
    This app counts the nucleotide composition of query DNA
""")


#####################
# Input Text Box
#####################

st.header('Enter DNA sequence:')

sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

# sequence = st.sidebar.text_area("Sequence input", sequence_input, height=250)
seq = st.text_area("Sequence Input", sequence_input, height = 250)
seq = seq.splitlines()
seq = seq[1:]
seq = ''.join(seq)


st.write("---")

st.header("Input(DNA Query)")
st.write(seq)

st.write("---")

st.header('Output (DNA Nucleotide Count)')

# Print Dictionary
st.subheader('1. Print dictionary')
def DNA_nucleotide_count(seq):
    d = dict({
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('G', seq.count('G')),
        ('C', seq.count('C'))
    })
    return d

X = DNA_nucleotide_count(seq)
st.write(X)


# Print Text
st.subheader('2. Print Text')
st.write(f"There are {str(X['A'])} adenine (A)")
st.write(f"There are {str(X['T'])} thymine (T)")
st.write(f"There are {str(X['G'])} guanine (G)")
st.write(f"There are {str(X['C'])} cytosine (C)")


# Display DataFrame
st.subheader("3. Display DataFrame")
df = pd.DataFrame.from_dict(X, orient = 'index')
df = df.rename({0: 'count'}, axis = 'columns')
df.reset_index(inplace = True)
df = df.rename(columns = {'index': 'nucleotide'})
st.write(df)

# Display Bar Chart Using Altair
st.subheader('4. Display Bar chart')
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)
p = p.properties(
    width=alt.Step(80)  # controls width of bar.
)
st.write(p)



































