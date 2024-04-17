import streamlit as st
import spacy
import en_core_web_sm
from newspaper import Article
from spacy import displacy

nlp = en_core_web_sm.load()

st.title("NLP ASSIGNMENT")


 
# Create a button, that when clicked, shows a text
if(st.button("About")):
    st.text("FIRST ASSIGNMENT ON NLP")


status = st.radio("SELECT ONE OF THE OPTIONS: ", ('ENTER URL', 'ENTER TEXT'))
 

# Create box url,that when clicked  provide option to input url
if status=="ENTER URL":
    url=st.text_input("enter url")
    if st.button("ANALIZE"):
        article=Article(url)
        article.download()
        article.parse()
        doc=nlp(article.text)
        displacy.render(doc, jupyter=False, style='ent')
        st.markdown(displacy.render(doc,style='ent',jupyter=False),unsafe_allow_html=True)

# Create box url,that when clicked  provide option to input paragraph
else:
    paragraph=st.text_area("ENTER TEXT")
    if st.button("ANALIZE"):
        doc=nlp(paragraph)
        displacy.render(doc, jupyter=False, style='ent')
        st.markdown(displacy.render(doc,style='ent',jupyter=False),unsafe_allow_html=True)