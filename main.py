import streamlit as st
import pickle
import nltk
from nltk.corpus import stopwords
import string
from nltk.stem.porter import PorterStemmer


#function for preprocessing
def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    y = []
    
    for i in text:
        if i.isalnum():
            y.append(i)
    text = y[:]
    y.clear()
    
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
            
    text = y[:]
    y.clear()
    
    #stemming
    ps = PorterStemmer()
    for i in text:
        y.append(ps.stem(i))
    
    return " ".join(y)


tfdif = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('modelmnb.pkl', 'rb'))

st.header("Email/Sms Spam Classifier",divider='rainbow')
input_sms = st.text_area("Enter the :blue[_message_] :mailbox_with_mail: :")

if st.button('Predict:heavy_check_mark:',type="primary"):
    # 1.preprocess
    transform_sms = transform_text(input_sms)
    # 2.veectorize
    vector_input = tfdif.transform([transform_sms])
    # 3.predict
    result = model.predict(vector_input)[0]
    # 4.display
    if result ==1:
        st.header("Spam!:skull:")
    else:
        st.header("Not Spam")


